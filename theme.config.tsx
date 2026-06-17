import React from 'react'
import { DocsThemeConfig } from 'nextra-theme-docs'

const config: DocsThemeConfig = {
  logo: (
    <span style={{ fontWeight: 700, fontSize: '1.2rem' }}>
      📚 FDU Sharing
    </span>
  ),
  search: {
    placeholder: '搜索课程...',
  },
  project: {
    link: 'https://github.com/victkk/FDU-Sharing',
  },
  docsRepositoryBase: 'https://github.com/victkk/FDU-Sharing/tree/main',
  footer: {
    content: (
      <span>
        Made with ❤️ by FDU CS Students | {new Date().getFullYear()} |{' '}
        <a href="https://github.com/victkk/FDU-Sharing" target="_blank">
          欢迎贡献
        </a>
      </span>
    ),
  },
  head: (
    <>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta name="description" content="FDU Sharing" />
      <title>FDU Sharing</title>
    </>
  ),
  sidebar: {
    defaultMenuCollapseLevel: 2,
    toggleButton: true,
  },
  toc: {
    backToTop: true,
  },
  editLink: {
    content: '在 GitHub 上编辑此页 →'
  },
  feedback: {
    content: '有问题？提交反馈 →',
    labels: 'feedback',
  },
  navigation: {
    prev: true,
    next: true,
  },
  gitTimestamp: ({ timestamp }) => (
    <span>最后更新于 {timestamp.toLocaleDateString('zh-CN')}</span>
  ),
}

export default config
