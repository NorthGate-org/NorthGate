
// Constants
const NORTHGATE_WS_URL = `ws://127.0.0.1:${getPort()}/ws`;

const ACTIONS = {
  LOAD_LOCAL_SITES: "load_local_sites",
  ERROR_MESSAGE: "error_message"
};

const INTERFACE_ELEMENTS_IDS = {
  LOADING_MESSAGE: "northgate_loading_message",
  LOADING_ALERT: "northgate_loading_alert",
  LOADING_SPINNER: "northgate_loading_spinner"
};

// Data
const localSites = [];

// Utils
function getPort() {
  const port = location.host.split(":")[1];
  return port;
}

// INIT
$.when( $.ready ).then(function() {
  console.log("NorthGate application starting...");

  const ws = new WebSocket(NORTHGATE_WS_URL);

  ws.onopen = function() {
    console.log("WebSocket connection established.");

    // Load local sites
    $(`#${INTERFACE_ELEMENTS_IDS.LOADING_MESSAGE}`).html("Loading local sites...");
    ws.send(JSON.stringify({ action: ACTIONS.LOAD_LOCAL_SITES }));
  };

  ws.onmessage = function(event) {
    const message = JSON.parse(event.data);
    if (message.action === ACTIONS.LOAD_LOCAL_SITES) {
      // Loaded local sites
      console.log("Local sites loaded:", message.data);
      localSites.length = 0;
      message.data.forEach(site => localSites.push(site));

    } else if (message.action === ACTIONS.ERROR_MESSAGE) {
      // Error handling
      console.error("Error message received:", message.message);
      if(localSites.length === 0) {
        $(`#${INTERFACE_ELEMENTS_IDS.LOADING_MESSAGE}`).hide();
        $(`#${INTERFACE_ELEMENTS_IDS.LOADING_SPINNER}`).hide();
        $(`#${INTERFACE_ELEMENTS_IDS.LOADING_ALERT}`).html(message.message).show();
      }
    }
  };

  ws.onclose = function() {
    console.log("WebSocket connection closed.");
  };

  ws.onerror = function(error) {
    console.error("WebSocket error:", error);
  };
});
