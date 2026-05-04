// @ts-ignore
import clipboardScript from "./scripts/clipboard.inline"
import clipboardStyle from "./styles/clipboard.scss"
import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const Body: QuartzComponent = ({ children }: QuartzComponentProps) => {
  return (
    <div id="quartz-body">
      <div id="reading-progress" aria-hidden="true" />
      <button id="back-to-top" aria-label="Voltar ao topo">↑</button>
      {children}
    </div>
  )
}

const scrollScript = `
;(function () {
  var progress = document.getElementById('reading-progress')
  var btn = document.getElementById('back-to-top')
  function updateScroll () {
    var h = document.documentElement
    var pct = h.scrollHeight - h.clientHeight
    if (progress) progress.style.width = (pct > 0 ? (h.scrollTop / pct) * 100 : 0) + '%'
    if (btn) btn.classList.toggle('visible', h.scrollTop > 300)
  }
  document.addEventListener('nav', function () {
    window.removeEventListener('scroll', updateScroll)
    window.addEventListener('scroll', updateScroll, { passive: true })
    updateScroll()
    if (btn) {
      var newBtn = btn.cloneNode(true)
      btn.parentNode.replaceChild(newBtn, btn)
      btn = newBtn
      btn.addEventListener('click', function () {
        window.scrollTo({ top: 0, behavior: 'smooth' })
      })
    }
  })
  window.addEventListener('scroll', updateScroll, { passive: true })
  if (btn) btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  })
})()
`

Body.afterDOMLoaded = clipboardScript + scrollScript
Body.css = clipboardStyle

export default (() => Body) satisfies QuartzComponentConstructor
