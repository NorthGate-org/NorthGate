
const NORTHGATE_WS_URL = `ws://127.0.0.1:${getPort()}/ws`;

const ACTIONS = {
  LOAD_LOCAL_SITES: "load_local_sites"
};

const INTERFACE_ELEMENTS_IDS = {
  LOADING_MESSAGE: "northgate_loading_message"
};

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
    console.log("WebSocket message received:", event.data);
  };
  ws.onclose = function() {
    console.log("WebSocket connection closed.");
  };
  ws.onerror = function(error) {
    console.error("WebSocket error:", error);
  };
});
