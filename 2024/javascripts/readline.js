const data = [
    { lineNumber: 1, firstLetters: "", fullSentence: "" },
    { lineNumber: 1, firstLetters: "", fullSentence: "bodhisattva avalokiteshvara"},
    { lineNumber: 1, firstLetters: "", fullSentence: "while deeply immersed in prajna paramita"},
    { lineNumber: 1, firstLetters: "", fullSentence: "clearly perceived the empty nature of the five skandhas"},
    { lineNumber: 1, firstLetters: "", fullSentence: "and transcended all suffering"},
    { lineNumber: 1, firstLetters: "", fullSentence: "shariputra form is not different from emptiness"},
    { lineNumber: 1, firstLetters: "", fullSentence: "emptiness is not different from form"},
    { lineNumber: 1, firstLetters: "", fullSentence: "form is emptiness"},
    { lineNumber: 1, firstLetters: "", fullSentence: "emptiness is form"},
    { lineNumber: 1, firstLetters: "", fullSentence: "so it is with feeling conception volition and consciousness"},
    { lineNumber: 1, firstLetters: "", fullSentence: "shariputra all dharmas are empty in character"},
    { lineNumber: 1, firstLetters: "", fullSentence: "neither arising nor ceasing"},
    { lineNumber: 1, firstLetters: "", fullSentence: "neither impure nor pure"},
    { lineNumber: 1, firstLetters: "", fullSentence: "neither increasing nor decreasing"},
    { lineNumber: 1, firstLetters: "", fullSentence: "therefore in emptiness"},
    { lineNumber: 1, firstLetters: "", fullSentence: "there is no form"},
    { lineNumber: 1, firstLetters: "", fullSentence: "there is no feeling conception volition or consciousness"},
    { lineNumber: 1, firstLetters: "", fullSentence: "no eye ear nose tongue body or mind"},
    { lineNumber: 1, firstLetters: "", fullSentence: "no form sound smell taste touch or dharmas"},
    { lineNumber: 1, firstLetters: "", fullSentence: "no realm of vision and so forth"},
    { lineNumber: 1, firstLetters: "", fullSentence: "up to no realm of mind-consciousness"},
    { lineNumber: 1, firstLetters: "", fullSentence: "no ignorance or ending of ignorance and so forth"},
    { lineNumber: 1, firstLetters: "", fullSentence: "up to no aging and death or ending of aging and death"},
    { lineNumber: 1, firstLetters: "", fullSentence: "there is no suffering no cause no extinction no path"},
    { lineNumber: 1, firstLetters: "", fullSentence: "there is no wisdom and no attainment"},
    { lineNumber: 1, firstLetters: "", fullSentence: "there is nothing to be attained by way of prajna paramita"},
    { lineNumber: 1, firstLetters: "", fullSentence: "the bodhisattva's mind is free from hindrances"},
    { lineNumber: 1, firstLetters: "", fullSentence: "with no hindrances there is no fear"},
    { lineNumber: 1, firstLetters: "", fullSentence: "freed from all distortion and delusion ultimate nirvana is reached"},
    { lineNumber: 1, firstLetters: "", fullSentence: "by way of prajna paramita buddhas of the past present and future "},
    { lineNumber: 1, firstLetters: "", fullSentence: "attain anuttara-samyak-sambodhi"},
    { lineNumber: 1, firstLetters: "", fullSentence: "therefore prajna paramita is the great powerful mantra"},
    { lineNumber: 1, firstLetters: "", fullSentence: "the great enlightening mantra"},
    { lineNumber: 1, firstLetters: "", fullSentence: "the supreme and peerless mantra"},
    { lineNumber: 1, firstLetters: "", fullSentence: "it can remove all suffering"},
    { lineNumber: 1, firstLetters: "", fullSentence: "this is the truth beyond all doubt"},
    { lineNumber: 1, firstLetters: "", fullSentence: "and the prajna paramita mantra is spoken thus"},
    { lineNumber: 1, firstLetters: "", fullSentence: "gate gate paragate parasamgate bodhi svaha"}
  ];

  
  let currentLine = 0;
  
  function createLine(lineData) {
    const lineElement = document.createElement('div');
    lineElement.textContent = lineData.firstLetters;
    lineElement.dataset.fullSentence = lineData.fullSentence;
    document.getElementById('content').appendChild(lineElement);
  }
  
  function revealLine() {
    const lines = document.querySelectorAll('#content div');
    if (currentLine < lines.length) {
      lines[currentLine].textContent = lines[currentLine].dataset.fullSentence;
      currentLine++;
    }
  }
  
  // Create initial lines
  data.forEach(createLine);
  
  const revealButton = document.getElementById('reveal_line');
  revealButton.addEventListener('click', revealLine);