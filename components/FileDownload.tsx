import React from 'react'

interface FileDownloadProps {
  name: string
  path: string
  size?: string
  date?: string
  type?: 'pdf' | 'doc' | 'zip' | 'other'
}

const typeIcons: Record<string, string> = {
  pdf: '📕',
  doc: '📘',
  zip: '📦',
  other: '📄',
}

const typeColors: Record<string, string> = {
  pdf: '#e74c3c',
  doc: '#3498db',
  zip: '#f39c12',
  other: '#95a5a6',
}

export function FileDownload({ 
  name, 
  path, 
  size, 
  date,
  type = 'pdf' 
}: FileDownloadProps) {
  const icon = typeIcons[type] || typeIcons.other
  const color = typeColors[type] || typeColors.other

  return (
    <a
      href={path}
      download
      style={{
        display: 'flex',
        alignItems: 'center',
        padding: '12px 16px',
        marginBottom: '8px',
        borderRadius: '8px',
        border: '1px solid #e1e5e9',
        textDecoration: 'none',
        color: 'inherit',
        transition: 'all 0.2s ease',
        backgroundColor: 'var(--nextra-bg)',
      }}
      onMouseEnter={(e) => {
        e.currentTarget.style.borderColor = color
        e.currentTarget.style.transform = 'translateX(4px)'
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.borderColor = '#e1e5e9'
        e.currentTarget.style.transform = 'translateX(0)'
      }}
    >
      <span style={{ fontSize: '1.5rem', marginRight: '12px' }}>{icon}</span>
      <div style={{ flex: 1 }}>
        <div style={{ fontWeight: 500 }}>{name}</div>
        <div style={{ fontSize: '0.85rem', color: '#666', marginTop: '2px' }}>
          {size && <span style={{ marginRight: '12px' }}>📦 {size}</span>}
          {date && <span>📅 {date}</span>}
        </div>
      </div>
      <span style={{ 
        fontSize: '1.2rem',
        color: color,
      }}>
        ⬇️
      </span>
    </a>
  )
}

export default FileDownload


