import { ref, computed, onMounted, onUnmounted } from 'vue'
import volumesData from '~/data/volumes.json'

const currentVolume = ref(1)
const tabByVolume = ref<Record<number, number>>({})

export function useTerminal() {
  const volumes = volumesData.volumes

  const activeVolume = computed(() => volumes.find(v => v.id === currentVolume.value) || volumes[0])
  const currentTab = computed(() => tabByVolume.value[currentVolume.value] ?? 0)

  function switchVolume(id: number) {
    currentVolume.value = id
    if (tabByVolume.value[id] === undefined) tabByVolume.value[id] = 0
  }

  function switchTab(index: number) {
    tabByVolume.value = { ...tabByVolume.value, [currentVolume.value]: index }
  }

  function handleKey(e: KeyboardEvent) {
    if (e.key === 'Escape') {
      const modal = document.getElementById('about-modal')
      if (modal) modal.style.display = 'none'
      return
    }
    const vol = volumes.find(v => v.id === currentVolume.value)
    if (!vol || vol.type === 'install') return
    const max = vol.count ?? 0
    const cur = currentTab.value
    if (e.key === 'ArrowRight' && cur < max) switchTab(cur + 1)
    if (e.key === 'ArrowLeft' && cur > 0) switchTab(cur - 1)
  }

  if (import.meta.client) {
    onMounted(() => window.addEventListener('keydown', handleKey))
    onUnmounted(() => window.removeEventListener('keydown', handleKey))
  }

  return { volumes, currentVolume, currentTab, activeVolume, switchVolume, switchTab }
}
