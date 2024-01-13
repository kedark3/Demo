const text = 'This is the text I want to write to a file'
const fileName = 'links.txt'
const blob = new Blob([text], { type: 'text/plain' })


function onButtonClick() {
  const url = window.URL.createObjectURL(blob)
  const a = document.createElement("a")
  a.href = url
  a.download = fileName
  a.click()
  window.URL.revokeObjectURL(url)
}