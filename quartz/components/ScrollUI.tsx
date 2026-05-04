/**
 * ScrollUI — Barra de progresso de leitura + botão back-to-top
 *
 * Componente customizado (fora do core quartz/quartz/).
 * Injetado via sharedPageComponents.afterBody em quartz.layout.ts.
 */
import { QuartzComponent, QuartzComponentConstructor } from "../quartz/components/types"

const ScrollUI: QuartzComponent = () => {
  return <button id="back-to-top" aria-label="Voltar ao topo">↑</button>
}

ScrollUI.afterDOMLoaded = `
;(function () {
  var btn = document.getElementById('back-to-top')
  if (!btn) return
  function onScroll() {
    btn.classList.toggle('visible', document.documentElement.scrollTop > 300)
  }
  function onClick() {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
  function setup() {
    window.addEventListener('scroll', onScroll, { passive: true })
    btn.addEventListener('click', onClick)
    onScroll()
  }
  document.addEventListener('nav', setup)
  setup()
})()
`

export default (() => ScrollUI) satisfies QuartzComponentConstructor
