import sqlite3
import os
from pathlib import Path
from threading import local

from northgate.constants import DB_PATH
from northgate.models.site import Site
from northgate.logger import logger

def get_local_sites():
    logger.info("Loading local sites...")
    local_sites = []

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM {} WHERE local = 1".format(Site.database_table))
        local_sites_rows = cursor.fetchall()
        # Load current local sites 
        for row in local_sites_rows:
            site = Site.fromRow(row)
            local_sites.append(site)

        # Check if local sites have been deleted
        for site in local_sites[:]:
            if not os.path.exists(site.path):
                cursor.execute("DELETE FROM {} WHERE id = ?".format(Site.database_table), (site.id,))
                conn.commit()
                logger.warning("Local site deleted: {}".format(site.path))
                local_sites.remove(site)

        # Add/Update local sites 
        base_dir = Path(__file__).resolve().parent.parent.parent
        sites_folder = os.path.join(base_dir.absolute(), 'sites')
        logger.info("Scanning local sites in folder: {}".format(sites_folder))
        for root, dirs, files in os.walk(sites_folder):
            if root[len(sites_folder):].count(os.sep) < 2:
                for filename in files:
                    if filename == "site.yaml":
                        # Check if site exists, if so update it
                        site_path = os.path.join(root, filename)
                        logger.debug("Found site.yaml: {}".format(site_path))
                        try:
                            with open(site_path, 'r') as f:
                                yaml_data = f.read()
                                existing_site = next((s for s in local_sites if s.path == site_path), None)
                                if existing_site:
                                    # Update the existing site
                                    updated_site = Site.fromYaml(existing_site.id, site_path, yaml_data)
                                    updated_site.local = True
                                    local_sites[local_sites.index(existing_site)] = updated_site
                                    # Update the site in the database
                                    statement = updated_site.update_statement()
                                    cursor.execute(statement[0], statement[1])
                                    conn.commit()
                                    logger.info("Local site updated: {}".format(site_path))
                                else:
                                    # Add new site
                                    new_site = Site.fromYaml(None, site_path, yaml_data)
                                    new_site.local = True
                                    local_sites.append(new_site)
                                    # Add the site in the database
                                    statement = new_site.insert_statement()
                                    cursor.execute(statement[0], statement[1])
                                    conn.commit()
                                    logger.info("Local site added: {}".format(site_path))
                        except Exception as e:
                            logger.error("Failed to process site.yaml at {}: {}".format(site_path, e))
                            raise e

    return local_sites
