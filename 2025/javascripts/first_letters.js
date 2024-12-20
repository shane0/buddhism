const data = [
    { lineNumber: 1, firstLetters: "ba", fullSentence: "bodhisattva avalokiteshvara"},
    { lineNumber: 1, firstLetters: "wdiipp", fullSentence: "while deeply immersed in prajna paramita"},
    { lineNumber: 1, firstLetters: "cptenotfs", fullSentence: "clearly perceived the empty nature of the five skandhas"},
    { lineNumber: 1, firstLetters: "atas", fullSentence: "and transcended all suffering"},
    { lineNumber: 1, firstLetters: "sfindfe", fullSentence: "shariputra form is not different from emptiness"},
    { lineNumber: 1, firstLetters: "eindff", fullSentence: "emptiness is not different from form"},
    { lineNumber: 1, firstLetters: "fie", fullSentence: "form is emptiness"},
    { lineNumber: 1, firstLetters: "eif", fullSentence: "emptiness is form"},
    { lineNumber: 1, firstLetters: "siiwfcvac", fullSentence: "so it is with feeling conception volition and consciousness"},
    { lineNumber: 1, firstLetters: "sadaeic", fullSentence: "shariputra all dharmas are empty in character"},
    { lineNumber: 1, firstLetters: "nanc", fullSentence: "neither arising nor ceasing"},
    { lineNumber: 1, firstLetters: "ninp", fullSentence: "neither impure nor pure"},
    { lineNumber: 1, firstLetters: "nind", fullSentence: "neither increasing nor decreasing"},
    { lineNumber: 1, firstLetters: "tie", fullSentence: "therefore in emptiness"},
    { lineNumber: 1, firstLetters: "tinf", fullSentence: "there is no form"},
    { lineNumber: 1, firstLetters: "tinfcvoc", fullSentence: "there is no feeling conception volition or consciousness"},
    { lineNumber: 1, firstLetters: "neentbom", fullSentence: "no eye ear nose tongue body or mind"},
    { lineNumber: 1, firstLetters: "nfssttod", fullSentence: "no form sound smell taste touch or dharmas"},
    { lineNumber: 1, firstLetters: "nrovasf", fullSentence: "no realm of vision and so forth"},
    { lineNumber: 1, firstLetters: "utnrom", fullSentence: "up to no realm of mind-consciousness"},
    { lineNumber: 1, firstLetters: "nioeoiasf", fullSentence: "no ignorance or ending of ignorance and so forth"},
    { lineNumber: 1, firstLetters: "utnaadoeoaad", fullSentence: "up to no aging and death or ending of aging and death"},
    { lineNumber: 1, firstLetters: "tinsncnenp", fullSentence: "there is no suffering no cause no extinction no path"},
    { lineNumber: 1, firstLetters: "tinwana", fullSentence: "there is no wisdom and no attainment"},
    { lineNumber: 1, firstLetters: "tintbabwopp", fullSentence: "there is nothing to be attained by way of prajna paramita"},
    { lineNumber: 1, firstLetters: "tbmiffh", fullSentence: "the bodhisattva's mind is free from hindrances"},
    { lineNumber: 1, firstLetters: "wnhtinf", fullSentence: "with no hindrances there is no fear"},
    { lineNumber: 1, firstLetters: "ffadadunir", fullSentence: "freed from all distortion and delusion ultimate nirvana is reached"},
    { lineNumber: 1, firstLetters: "bwoppbotppaf", fullSentence: "by way of prajna paramita buddhas of the past present and future "},
    { lineNumber: 1, firstLetters: "aa", fullSentence: "attain anuttara-samyak-sambodhi"},
    { lineNumber: 1, firstLetters: "tppitgpm", fullSentence: "therefore prajna paramita is the great powerful mantra"},
    { lineNumber: 1, firstLetters: "tgem", fullSentence: "the great enlightening mantra"},
    { lineNumber: 1, firstLetters: "tsapm", fullSentence: "the supreme and peerless mantra"},
    { lineNumber: 1, firstLetters: "icras", fullSentence: "it can remove all suffering"},
    { lineNumber: 1, firstLetters: "tittbad", fullSentence: "this is the truth beyond all doubt"},
    { lineNumber: 1, firstLetters: "atppmist", fullSentence: "and the prajna paramita mantra is spoken thus"},
    { lineNumber: 1, firstLetters: "ggppbs", fullSentence: "gate gate paragate parasamgate bodhi svaha"}
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
  
  const revealButton = document.getElementById('reveal');
  revealButton.addEventListener('click', revealLine);

  const revealButtonBottom = document.getElementById('reveal_bottom');
  revealButtonBottom.addEventListener('click', revealLine);