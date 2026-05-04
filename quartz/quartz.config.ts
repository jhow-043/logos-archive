import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"
import { isFolderPath } from "./quartz/util/path"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "Logos Archive",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "pt-BR",
    baseUrl: "jhow-043.github.io/logos-archive",
    ignorePatterns: ["_stubs/templates", "private", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          // Catppuccin Latte
          light: "#eff1f5",
          lightgray: "#ccd0da",
          gray: "#9ca0b0",
          darkgray: "#5c5f77",
          dark: "#4c4f69",
          secondary: "#8839ef",
          tertiary: "#7287fd",
          highlight: "rgba(136, 57, 239, 0.08)",
          textHighlight: "rgba(223, 142, 29, 0.35)",
        },
        darkMode: {
          // Catppuccin Mocha
          light: "#1e1e2e",
          lightgray: "#313244",
          gray: "#6c7086",
          darkgray: "#bac2de",
          dark: "#cdd6f4",
          secondary: "#cba6f7",
          tertiary: "#b4befe",
          highlight: "rgba(203, 166, 247, 0.12)",
          textHighlight: "rgba(249, 226, 175, 0.25)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage({
        sort: (f1, f2) => {
          // Folders (index pages) always first
          const f1IsFolder = isFolderPath(f1.slug ?? "")
          const f2IsFolder = isFolderPath(f2.slug ?? "")
          if (f1IsFolder !== f2IsFolder) return f1IsFolder ? -1 : 1
          // MOC files second (tipo: moc in frontmatter)
          const f1IsMoc = (f1.frontmatter as Record<string, unknown>)?.tipo === "moc"
          const f2IsMoc = (f2.frontmatter as Record<string, unknown>)?.tipo === "moc"
          if (f1IsMoc !== f2IsMoc) return f1IsMoc ? -1 : 1
          // Then date descending
          if (f1.dates && f2.dates) return f2.dates.modified.getTime() - f1.dates.modified.getTime()
          if (f1.dates && !f2.dates) return -1
          if (!f1.dates && f2.dates) return 1
          // Fallback: alphabetical
          const t1 = f1.frontmatter?.title.toLowerCase() ?? ""
          const t2 = f2.frontmatter?.title.toLowerCase() ?? ""
          return t1.localeCompare(t2)
        },
      }),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
