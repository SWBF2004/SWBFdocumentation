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

    function showEntry(entry) {
      console.log(entry)
      return `<li>${entry.begin}<span class="highlight">${entry.match}</span>${entry.end}</li>`;
    }

    function showFile(file) {
      return `<ul><a href="${file[0]}.html" target="document">${file[0]}</a>:${file[1].map(entry => showEntry(entry)).join("")}</ul>`
    }

    searchResults.innerHTML = Object.entries(data).map(file => showFile(file)).join("<br>");

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
