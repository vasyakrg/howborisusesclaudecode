<script setup lang="ts">
import { ref, computed } from 'vue'
import { useTerminal } from '~/composables/useTerminal'
import contentRu from '~/data/content.ru.json'

const { volumes, currentVolume, currentTab, switchVolume, switchTab } = useTerminal()

const allAreas = computed(() => contentRu.data as Array<{ idx: number; label: string; tabs: Array<{ label: string; html: string }> }>)

function getArea(partIdx: number) {
  return allAreas.value[partIdx]
}

function getTabLabel(rawLabel: string) {
  const parts = rawLabel.split(/\s+/)
  const num = parts[0] || '~'
  const name = parts.slice(1).join(' ') || rawLabel
  return { num, name }
}

const progress = computed(() => {
  const vol = volumes.find(v => v.id === currentVolume.value)
  if (!vol || vol.type === 'install') return ''
  const idx = currentTab.value
  if (idx === 0) return ''
  return `${idx}/${vol.count}`
})

const aboutOpen = ref(false)

function handleContentClick(e: MouseEvent) {
  const target = e.target as HTMLElement
  const btn = target.closest('button.nav-btn') as HTMLButtonElement | null
  if (!btn) return
  const raw = btn.getAttribute('onclick') || ''
  const m = raw.match(/switchTab\((\d+)\)/)
  if (m) {
    e.preventDefault()
    switchTab(parseInt(m[1], 10))
  }
}
</script>

<template>
  <div>
    <div class="terminal-window">
      <div class="title-bar">
        <div class="window-controls">
          <div class="window-control close"></div>
          <div class="window-control minimize"></div>
          <div class="window-control maximize"></div>
        </div>
        <div class="window-title">claude-cli — <span>Как Борис использует Claude Code</span></div>
        <button class="title-bar-nav" @click="aboutOpen = true">О сайте</button>
        <NuxtLink class="title-bar-nav" to="/claudeonomics">Клодономика</NuxtLink>
      </div>

      <div class="volume-selector">
        <template v-for="v in volumes" :key="v.id">
          <span v-if="v.type === 'install' && v.id === 8" class="volume-divider"></span>
          <button
            :class="['volume-btn', v.type === 'install' ? 'install-btn' : '', currentVolume === v.id ? 'active' : '']"
            @click="switchVolume(v.id)"
          >
            <template v-if="v.type === 'install'">
              <svg v-if="v.icon === 'download'" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <svg v-else width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
              {{ v.label }}
            </template>
            <template v-else>
              {{ v.label }}
              <span v-if="v.badge" class="volume-meta">
                <span class="volume-count">{{ v.count }}</span>
                <span class="volume-badge">{{ v.badge }}</span>
              </span>
              <span v-else class="volume-count">{{ v.count }}</span>
            </template>
          </button>
        </template>
      </div>

      <template v-for="v in volumes" :key="'tabbar-'+v.id">
        <div
          v-if="v.type === 'part'"
          :class="['tab-bar', currentVolume === v.id ? 'active' : '']"
          :data-volume="v.id"
        >
          <button
            v-for="(t, i) in (getArea(v.partIdx)?.tabs || [])"
            :key="i"
            :class="['tab', (currentVolume === v.id && currentTab === i) ? 'active' : '']"
            @click="switchTab(i)"
          >
            <span class="tab-number">{{ getTabLabel(t.label).num }}</span>
            <span class="tab-label">{{ getTabLabel(t.label).name }}</span>
          </button>
        </div>
      </template>

      <template v-for="v in volumes" :key="'area-'+v.id">
        <div
          :class="['content-area', currentVolume === v.id ? 'active' : '']"
          :data-volume="v.id"
          @click="handleContentClick"
        >
          <template v-if="v.type === 'install'">
            <div v-if="getArea(v.partIdx)?.tabs?.[0]" class="tab-content active" v-html="getArea(v.partIdx).tabs[0].html"></div>
          </template>
          <template v-else>
            <div
              v-for="(t, i) in (getArea(v.partIdx)?.tabs || [])"
              :key="i"
              :class="['tab-content', (currentVolume === v.id && currentTab === i) ? 'active' : '']"
              v-html="t.html"
            ></div>
          </template>
        </div>
      </template>

      <div class="status-bar">
        <div class="status-item">
          <div class="status-dot"></div>
          claude-cli подключён
        </div>
        <div class="status-item">
          <span id="progress-indicator" style="margin-right: 12px; color: var(--claude-orange);">{{ progress }}</span>
          opus-4.7 · размышляет<span class="thinking-dots"></span>
        </div>
      </div>

      <div class="footer">
        По материалам <a href="https://x.com/bcherny/status/2007179832300581177" target="_blank" rel="noopener noreferrer">треда @bcherny</a>
        <div style="margin-top: 8px; color: var(--text-secondary);">
          Ctrl+C, Ctrl+V, Ctrl+Ship. Оригинал — <a href="https://github.com/carolinacherry" target="_blank" rel="noopener noreferrer">@CarolinaCherry</a>. Русский порт — для сообщества.
        </div>
      </div>
    </div>

    <div style="text-align: center; padding: 0 0 16px; font-family: 'JetBrains Mono', monospace; font-size: 13px; color: #555; display: flex; align-items: center; justify-content: center; gap: 16px; flex-wrap: wrap;">
      <span>HowBorisUsesClaudeCode.ru — русская версия</span>
    </div>

    <div
      v-if="aboutOpen"
      id="about-modal"
      @click.self="aboutOpen = false"
      style="display:flex; position:fixed; inset:0; z-index:1000; background:rgba(0,0,0,0.7); backdrop-filter:blur(4px); align-items:center; justify-content:center;"
    >
      <div class="about-modal-card">
        <button
          @click="aboutOpen = false"
          style="position:absolute; top:12px; right:16px; background:none; border:none; color:var(--text-muted); font-size:18px; cursor:pointer; font-family:'JetBrains Mono',monospace; line-height:1;"
        >×</button>
        <p style="margin-bottom: 16px;">Оригинал собрал <a href="https://github.com/carolinacherry" target="_blank" rel="noopener" style="color: var(--blue-link); text-decoration: none;">@CarolinaCherry</a>. Не связан с Anthropic.</p>
        <p style="margin-bottom: 16px;">Борис Черны создал Claude Code в Anthropic. Он регулярно делится рабочими практиками в X, но советы разбросаны по десяткам тредов. Этот сайт собирает их в одном месте — структурированно, удобно для чтения и всегда актуально.</p>
        <p style="margin-bottom: 16px;">Весь контент — прямые цитаты и пересказ постов Бориса. Ничего не выдумано.</p>
        <p>Это фан-проект. Не официальный. Не спонсируется. Собрано в Claude Code — естественно.</p>
      </div>
    </div>
  </div>
</template>
