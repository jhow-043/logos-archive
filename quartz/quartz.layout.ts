import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import { FileTrieNode } from "./quartz/util/fileTrie"

// A MOC file has the same slug segment as its parent folder
// e.g. química/disciplina/disciplina → MOC of "disciplina" folder
const explorerSortFn = (a: FileTrieNode, b: FileTrieNode): number => {
  const isMoc = (node: FileTrieNode): boolean => {
    if (node.isFolder || !node.data) return false
    const parts = node.slug.split("/")
    return parts.length >= 2 && parts[parts.length - 1] === parts[parts.length - 2]
  }
  if (a.isFolder !== b.isFolder) return a.isFolder ? -1 : 1
  const aMoc = isMoc(a)
  const bMoc = isMoc(b)
  if (aMoc !== bMoc) return aMoc ? -1 : 1
  return a.displayName.localeCompare(b.displayName, undefined, { numeric: true, sensitivity: "base" })
}

const explorerMapFn = (node: FileTrieNode): void => {
  if (!node.isFolder && node.data) {
    const parts = node.slug.split("/")
    if (parts.length >= 2 && parts[parts.length - 1] === parts[parts.length - 2]) {
      node.displayName = "◆ " + node.displayName
    }
  }
}

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jhow-043/logos-archive",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      filterFn: (node) => node.name !== "_stubs",
      sortFn: explorerSortFn,
      mapFn: explorerMapFn,
      order: ["filter", "sort", "map"],
    }),
  ],
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
  ],
  afterBody: [
    Component.Graph(),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      filterFn: (node) => node.name !== "_stubs",
      sortFn: explorerSortFn,
      mapFn: explorerMapFn,
      order: ["filter", "sort", "map"],
    }),
  ],
  right: [
    Component.DesktopOnly(Component.Graph()),
  ],
}
