function main() {
  initWebsocket()
}

function initWebsocket() {
  let ws = new WebSocket(`ws://localhost:${parseInt(location.port) + 1}`);

  ws.onopen = function () {
    console.log("Websocket open");
  };

  ws.onclose = function () {
    console.log("Websocket closed");
  };

  ws.onmessage = function (evt) {
    const data = JSON.parse(evt.data)
    console.debug("Websocket response");
    console.debug(data);

    const searchResults = document.getElementById("search-results");
    if(!searchResults)
      return;

    function createEntry(entry) {
      return `<li>${entry.file}</li>${entry.match}<br>`;
    }

    searchResults.innerHTML = "<ul>" + data.map(o => createEntry(o)).join('<br>') + "</ul>";

  };

  document.ws = ws;
}

function search(term) {
  if(!document.ws || document.ws.readyState != WebSocket.OPEN)
    return;

  const searchTerm = document.getElementById("search-term");
  if(!searchTerm)
    return;

  document.ws.send(JSON.stringify({
    term: searchTerm.value
  }))
}
