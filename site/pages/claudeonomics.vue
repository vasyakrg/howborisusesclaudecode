<script setup lang="ts">
import { onMounted } from 'vue'

useHead({
  title: 'Клодономика — Claude Code',
  meta: [
    { name: 'description', content: 'Еженедельные коммиты AI-агентов на публичном GitHub с момента релиза Claude Code' }
  ]
})

onMounted(() => {
  // Загружаем скрипт с графиками только на клиенте, после гидратации.
  // Если источник данных недоступен, скрипт оставит статически отрендеренную разметку.
  const s = document.createElement('script')
  s.src = '/claudeonomics.js'
  s.defer = true
  document.body.appendChild(s)
})

// Статическая предотрендеренная разметка дашборда (переведена на русский).
// Содержит inline-SVG графики и таблицу-рейтинг. Клиентский скрипт может
// заменить содержимое #dash-root при наличии данных.
const dashHtml = `
      <div class="kpi-strip">
        <div class="kpi">
          <div class="kpi-label">Claude Code за неделю</div>
          <div class="kpi-value">2.72M</div>
          <div class="kpi-delta">WoW <span class="delta-up">▲ 5.7%</span></div>
        </div>
        <div class="kpi">
          <div class="kpi-label">За всё время</div>
          <div class="kpi-value">29.2M</div>
          <div class="kpi-delta">накопительно с мая 2025</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Доля Claude среди отслеживаемых</div>
          <div class="kpi-value">99.5%</div>
          <div class="kpi-delta">из 2.73M коммитов в неделю</div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Все отслеживаемые агенты за неделю</div>
          <div class="kpi-value small">2.73M</div>
          <div class="kpi-delta">WoW <span class="delta-up">▲ 5.7%</span></div>
        </div>
        <div class="kpi">
          <div class="kpi-label">Неделя по</div>
          <div class="kpi-value small">12 апр</div>
          <div class="kpi-delta">49 закрытых недель данных</div>
        </div>
      </div>
      <div class="chart-section">
        <div class="chart-header">
          <div>
            <div class="chart-title">Claude Code — коммитов в неделю</div>
            <div class="chart-subtitle">публичный GitHub, по дате коммиттера · терминальный CLI-агент</div>
          </div>
          <div class="chart-subtitle">2025-05-05 → 2026-04-12</div>
        </div>
        <div class="chart-box" id="hero-chart-box">
          <div id="hero-chart-mount">
            <svg id="hero-svg" class="chart-svg" viewBox="0 0 900 240" preserveAspectRatio="none">
                <defs>
                    <linearGradient id="heroGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%" style="stop-color:#E07A41;stop-opacity:0.28"></stop>
                        <stop offset="100%" style="stop-color:#E07A41;stop-opacity:0.02"></stop>
                    </linearGradient>
                </defs>
                <line class="chart-grid-line" x1="28" y1="70" x2="844" y2="70"></line><text class="chart-axis-label" x="24" y="73" text-anchor="end">2.24M</text><line class="chart-grid-line" x1="28" y1="120" x2="844" y2="120"></line><text class="chart-axis-label" x="24" y="123" text-anchor="end">1.50M</text><line class="chart-grid-line" x1="28" y1="170" x2="844" y2="170"></line><text class="chart-axis-label" x="24" y="173" text-anchor="end">748k</text>
                <path d="M28.0,219.7 L45.0,219.7 L62.0,219.2 L79.0,218.5 L96.0,217.9 L113.0,216.4 L130.0,215.1 L147.0,214.2 L164.0,214.2 L181.0,213.3 L198.0,213.1 L215.0,212.1 L232.0,211.4 L249.0,211.1 L266.0,210.6 L283.0,210.4 L300.0,210.9 L317.0,211.2 L334.0,211.5 L351.0,211.3 L368.0,211.7 L385.0,208.2 L402.0,207.1 L419.0,206.7 L436.0,201.9 L453.0,202.6 L470.0,203.0 L487.0,201.7 L504.0,202.2 L521.0,200.7 L538.0,199.2 L555.0,198.9 L572.0,197.1 L589.0,195.5 L606.0,187.4 L623.0,179.0 L640.0,171.9 L657.0,164.4 L674.0,158.3 L691.0,148.5 L708.0,139.9 L725.0,121.3 L742.0,107.8 L759.0,98.4 L776.0,82.8 L793.0,44.6 L810.0,40.1 L827.0,48.0 L844.0,38.2 L844.0,220.0 L28.0,220.0 Z" fill="url(#heroGrad)"></path>
                <path d="M28.0,219.7 L45.0,219.7 L62.0,219.2 L79.0,218.5 L96.0,217.9 L113.0,216.4 L130.0,215.1 L147.0,214.2 L164.0,214.2 L181.0,213.3 L198.0,213.1 L215.0,212.1 L232.0,211.4 L249.0,211.1 L266.0,210.6 L283.0,210.4 L300.0,210.9 L317.0,211.2 L334.0,211.5 L351.0,211.3 L368.0,211.7 L385.0,208.2 L402.0,207.1 L419.0,206.7 L436.0,201.9 L453.0,202.6 L470.0,203.0 L487.0,201.7 L504.0,202.2 L521.0,200.7 L538.0,199.2 L555.0,198.9 L572.0,197.1 L589.0,195.5 L606.0,187.4 L623.0,179.0 L640.0,171.9 L657.0,164.4 L674.0,158.3 L691.0,148.5 L708.0,139.9 L725.0,121.3 L742.0,107.8 L759.0,98.4 L776.0,82.8 L793.0,44.6 L810.0,40.1 L827.0,48.0 L844.0,38.2" class="chart-line hero" stroke="#E07A41"></path>
                <line id="hero-hover-line" class="chart-hover-line" stroke="#E07A41" x1="0" y1="20" x2="0" y2="220"></line>
                <circle id="hero-hover-dot" class="chart-hover-dot" fill="#E07A41" cx="0" cy="0" r="5"></circle>
                <circle cx="844" cy="38.18181818181819" r="4" fill="#E07A41"></circle>
                <rect id="hero-overlay" x="0" y="0" width="900" height="240" fill="transparent" style="cursor: crosshair;"></rect>
            </svg></div>
          <div class="chart-tooltip" id="hero-tooltip">
            <div class="chart-tooltip-count"><span id="hero-tooltip-count">0</span> коммитов</div>
            <div class="chart-tooltip-time" id="hero-tooltip-time">—</div>
          </div>
          <div class="chart-x-labels">
            <span>5 мая</span>
            <span>12 апр</span>
          </div>
        <div class="chart-end-logo" style="position: absolute; left: 835.613px; top: 50.1818px; width: 18px; height: 18px; color: rgb(224, 122, 65); pointer-events: none;"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="18" height="18" style="fill: rgb(224, 122, 65);"><path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z"></path></svg></div></div>
      </div>

      <div class="chart-section">
        <div class="chart-header">
          <div>
            <div class="chart-title">CLI-конкуренты — коммитов в неделю</div>
            <div class="chart-subtitle">терминальные агенты как Claude Code: Copilot CLI, Codex CLI, Gemini CLI (отдельная шкала)</div>
          </div>
          <div class="chart-subtitle">2025-06-23 → 2026-04-12</div>
        </div>
        <div class="chart-box" id="cli-chart-box">
          <div id="cli-chart-mount">
            <svg id="cli-svg" class="chart-svg small" viewBox="0 0 900 180" preserveAspectRatio="none">
                <line class="chart-grid-line" x1="28" y1="55" x2="844" y2="55"></line><text class="chart-axis-label" x="24" y="58" text-anchor="end">1.9k</text><line class="chart-grid-line" x1="28" y1="90" x2="844" y2="90"></line><text class="chart-axis-label" x="24" y="93" text-anchor="end">1.3k</text><line class="chart-grid-line" x1="28" y1="125" x2="844" y2="125"></line><text class="chart-axis-label" x="24" y="128" text-anchor="end">643</text>
                <path d="M286.7,158.9 L306.6,156.2 L326.5,157.8 L346.4,157.2 L366.3,156.3 L386.2,157.1 L406.1,153.4 L426.0,157.0 L446.0,155.7 L465.9,153.1 L485.8,156.2 L505.7,157.7 L525.6,156.7 L545.5,158.1 L565.4,157.2 L585.3,155.5 L605.2,154.1 L625.1,150.3 L645.0,149.1 L664.9,149.9 L684.8,142.7 L704.7,135.5 L724.6,130.3 L744.5,122.4 L764.4,119.3 L784.3,117.7 L804.2,112.8 L824.1,116.1 L844.0,104.2" class="chart-line" stroke="#f472b6"></path><path d="M127.5,151.4 L147.4,152.9 L167.3,157.6 L187.2,151.8 L207.1,149.8 L227.0,145.1 L246.9,147.9 L266.8,142.1 L286.7,145.8 L306.6,153.1 L326.5,149.4 L346.4,150.5 L366.3,146.9 L386.2,136.7 L406.1,141.5 L426.0,147.4 L446.0,138.3 L465.9,152.0 L485.8,156.8 L505.7,149.8 L525.6,146.5 L545.5,151.6 L565.4,152.9 L585.3,81.6 L605.2,139.4 L625.1,135.1 L645.0,96.9 L664.9,71.6 L684.8,95.2 L704.7,76.2 L724.6,87.7 L744.5,81.4 L764.4,54.0 L784.3,86.4 L804.2,80.7 L824.1,82.8 L844.0,89.8" class="chart-line" stroke="#4ade80"></path><path d="M28.0,141.6 L47.9,138.4 L67.8,152.4 L87.7,131.1 L107.6,153.5 L127.5,143.1 L147.4,134.1 L167.3,139.5 L187.2,146.1 L207.1,150.3 L227.0,126.8 L246.9,138.8 L266.8,44.7 L286.7,135.8 L306.6,148.1 L326.5,122.5 L346.4,135.9 L366.3,104.9 L386.2,123.9 L406.1,142.4 L426.0,149.4 L446.0,144.9 L465.9,134.3 L485.8,148.1 L505.7,144.7 L525.6,128.2 L545.5,141.5 L565.4,142.7 L585.3,129.8 L605.2,132.3 L625.1,123.0 L645.0,110.8 L664.9,103.9 L684.8,62.2 L704.7,99.0 L724.6,52.7 L744.5,61.6 L764.4,32.7 L784.3,55.1 L804.2,50.8 L824.1,60.4 L844.0,53.2" class="chart-line" stroke="#c084fc"></path>
                <circle cx="844.0" cy="104.2" r="3" fill="#f472b6"></circle><circle cx="844.0" cy="89.8" r="3" fill="#4ade80"></circle><circle cx="844.0" cy="53.2" r="3" fill="#c084fc"></circle>
                <line id="cli-hover-line" class="chart-hover-line" stroke="#888" x1="0" y1="20" x2="0" y2="160"></line>
                <circle id="cli-hover-dot" class="chart-hover-dot" fill="#fff" cx="0" cy="0" r="5"></circle>
                <rect id="cli-overlay" x="0" y="0" width="900" height="180" fill="transparent" style="cursor: crosshair;"></rect>
            </svg></div>
          <div class="chart-tooltip" id="cli-tooltip">
            <div class="chart-tooltip-label" id="cli-tooltip-label">—</div>
            <div class="chart-tooltip-count alt"><span id="cli-tooltip-count">0</span> коммитов</div>
            <div class="chart-tooltip-time" id="cli-tooltip-time">—</div>
          </div>
          <div class="chart-x-labels">
            <span>23 июн</span>
            <span>12 апр</span>
          </div>
        <div class="chart-end-logo" style="position: absolute; left: 835.613px; top: 65.2042px; width: 18px; height: 18px; color: rgb(192, 132, 252); pointer-events: none;"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="18" height="18" style="fill: rgb(192, 132, 252);"><path d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"></path></svg></div><div class="chart-end-logo" style="position: absolute; left: 835.613px; top: 101.801px; width: 18px; height: 18px; color: rgb(74, 222, 128); pointer-events: none;"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="18" height="18" style="fill: rgb(74, 222, 128);"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"></path></svg></div><div class="chart-end-logo" style="position: absolute; left: 835.613px; top: 121.801px; width: 18px; height: 18px; color: rgb(244, 114, 182); pointer-events: none;"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="18" height="18" style="fill: rgb(244, 114, 182);"><path d="M23.922 16.997C23.061 18.492 18.063 22.02 12 22.02 5.937 22.02.939 18.492.078 16.997A.641.641 0 0 1 0 16.741v-2.869a.883.883 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.098 10.098 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952C7.255 2.937 9.248 1.98 11.978 1.98c2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.841.841 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256Zm-11.75-5.992h-.344a4.359 4.359 0 0 1-.355.508c-.77.947-1.918 1.492-3.508 1.492-1.725 0-2.989-.359-3.782-1.259a2.137 2.137 0 0 1-.085-.104L4 11.746v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.359 4.359 0 0 1-.355-.508Zm2.328 3.25c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm-5 0c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm3.313-6.185c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path></svg></div></div>
      </div>

      <div class="chart-section">
        <div class="chart-header">
          <div>
            <div class="chart-title">Облачные / асинхронные конкуренты — коммитов в неделю</div>
            <div class="chart-subtitle">агенты, работающие как сервис, не в терминале: Copilot Coding Agent, Codex (ChatGPT)</div>
          </div>
          <div class="chart-subtitle">2025-05-19 → 2026-04-12</div>
        </div>
        <div class="chart-box" id="cloud-chart-box">
          <div id="cloud-chart-mount">
            <svg id="cloud-svg" class="chart-svg small" viewBox="0 0 900 180" preserveAspectRatio="none">
                <line class="chart-grid-line" x1="28" y1="55" x2="844" y2="55"></line><text class="chart-axis-label" x="24" y="58" text-anchor="end">8.5k</text><line class="chart-grid-line" x1="28" y1="90" x2="844" y2="90"></line><text class="chart-axis-label" x="24" y="93" text-anchor="end">5.7k</text><line class="chart-grid-line" x1="28" y1="125" x2="844" y2="125"></line><text class="chart-axis-label" x="24" y="128" text-anchor="end">2.8k</text>
                <path d="M28.0,154.2 L45.7,148.9 L63.5,147.7 L81.2,145.1 L99.0,146.6 L116.7,149.3 L134.4,146.4 L152.2,145.3 L169.9,139.0 L187.7,136.5 L205.4,136.3 L223.1,124.3 L240.9,133.8 L258.6,122.3 L276.3,122.5 L294.1,123.4 L311.8,121.2 L329.6,126.3 L347.3,125.4 L365.0,115.8 L382.8,109.9 L400.5,108.1 L418.3,105.8 L436.0,99.1 L453.7,85.2 L471.5,88.1 L489.2,82.3 L507.0,80.2 L524.7,69.5 L542.4,80.9 L560.2,85.2 L577.9,101.7 L595.7,92.6 L613.4,79.7 L631.1,81.8 L648.9,73.1 L666.6,64.2 L684.3,62.4 L702.1,58.4 L719.8,49.8 L737.6,39.0 L755.3,32.7 L773.0,38.1 L790.8,46.2 L808.5,46.2 L826.3,48.0 L844.0,44.6" class="chart-line" stroke="#60a5fa"></path><path d="M294.1,160.0 L311.8,156.0 L329.6,159.9 L347.3,160.0 L365.0,159.9 L382.8,159.9 L400.5,159.8 L418.3,159.7 L436.0,159.4 L453.7,159.6 L471.5,159.4 L489.2,159.3 L507.0,159.9 L524.7,159.9 L542.4,160.0 L560.2,159.9 L577.9,159.8 L595.7,159.7 L613.4,159.7 L631.1,159.7 L648.9,159.5 L666.6,159.5 L684.3,159.6 L702.1,155.1 L719.8,156.5 L737.6,155.4 L755.3,151.7 L773.0,157.3 L790.8,158.0 L808.5,158.6 L826.3,158.4 L844.0,158.8" class="chart-line" stroke="#f59e0b"></path>
                <circle cx="844.0" cy="44.6" r="3" fill="#60a5fa"></circle><circle cx="844.0" cy="158.8" r="3" fill="#f59e0b"></circle>
                <line id="cloud-hover-line" class="chart-hover-line" stroke="#888" x1="0" y1="20" x2="0" y2="160"></line>
                <circle id="cloud-hover-dot" class="chart-hover-dot" fill="#fff" cx="0" cy="0" r="5"></circle>
                <rect id="cloud-overlay" x="0" y="0" width="900" height="180" fill="transparent" style="cursor: crosshair;"></rect>
            </svg></div>
          <div class="chart-tooltip" id="cloud-tooltip">
            <div class="chart-tooltip-label" id="cloud-tooltip-label">—</div>
            <div class="chart-tooltip-count alt"><span id="cloud-tooltip-count">0</span> коммитов</div>
            <div class="chart-tooltip-time" id="cloud-tooltip-time">—</div>
          </div>
          <div class="chart-x-labels">
            <span>19 мая</span>
            <span>12 апр</span>
          </div>
        <div class="chart-end-logo" style="position: absolute; left: 835.613px; top: 56.6052px; width: 18px; height: 18px; color: rgb(96, 165, 250); pointer-events: none;"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="18" height="18" style="fill: rgb(96, 165, 250);"><path d="M23.922 16.997C23.061 18.492 18.063 22.02 12 22.02 5.937 22.02.939 18.492.078 16.997A.641.641 0 0 1 0 16.741v-2.869a.883.883 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.098 10.098 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952C7.255 2.937 9.248 1.98 11.978 1.98c2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.841.841 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256Zm-11.75-5.992h-.344a4.359 4.359 0 0 1-.355.508c-.77.947-1.918 1.492-3.508 1.492-1.725 0-2.989-.359-3.782-1.259a2.137 2.137 0 0 1-.085-.104L4 11.746v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.359 4.359 0 0 1-.355-.508Zm2.328 3.25c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm-5 0c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm3.313-6.185c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path></svg></div><div class="chart-end-logo" style="position: absolute; left: 835.613px; top: 170.769px; width: 18px; height: 18px; color: rgb(245, 158, 11); pointer-events: none;"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="18" height="18" style="fill: rgb(245, 158, 11);"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"></path></svg></div></div>
      </div>
      <div class="chart-section">
        <div class="chart-header">
          <div>
            <div class="chart-title">Рейтинг агентов — неделя с 6 апр по 12 апр</div>
            <div class="chart-subtitle">по количеству коммитов в неделю</div>
          </div>
        </div>
        <div class="chart-box" style="padding: 0;">
          <table class="leaderboard">
            <thead>
              <tr>
                <th style="width: 32px;">#</th>
                <th>Агент</th>
                <th class="hide-mobile">Тип</th>
                <th class="num">Коммитов/нед</th>
                <th class="num hide-mobile">Доля</th>
                <th class="num hide-mobile">WoW</th>
              </tr>
            </thead>
            <tbody>
              <tr style="--row-accent:#E07A41;">
                <td style="color: var(--text-muted);">1</td>
                <td>
                  <div class="agent-cell">
                    <span class="agent-logo" style="color:#E07A41"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M17.3041 3.541h-3.6718l6.696 16.918H24Zm-10.6082 0L0 20.459h3.7442l1.3693-3.5527h7.0052l1.3693 3.5528h3.7442L10.5363 3.5409Zm-.3712 10.2232 2.2914-5.9456 2.2914 5.9456Z"></path></svg></span>
                    <span>Claude Code</span>
                  </div>
                </td>
                <td class="hide-mobile"><span class="type-pill cli">CLI</span></td>
                <td class="num">2&nbsp;720&nbsp;382</td>
                <td class="num hide-mobile">99.5%</td>
                <td class="num hide-mobile"><span class="delta-up">▲ 5.7%</span></td>
              </tr>
              <tr style="--row-accent:#60a5fa;">
                <td style="color: var(--text-muted);">2</td>
                <td>
                  <div class="agent-cell">
                    <span class="agent-logo" style="color:#60a5fa"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.922 16.997C23.061 18.492 18.063 22.02 12 22.02 5.937 22.02.939 18.492.078 16.997A.641.641 0 0 1 0 16.741v-2.869a.883.883 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.098 10.098 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952C7.255 2.937 9.248 1.98 11.978 1.98c2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.841.841 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256Zm-11.75-5.992h-.344a4.359 4.359 0 0 1-.355.508c-.77.947-1.918 1.492-3.508 1.492-1.725 0-2.989-.359-3.782-1.259a2.137 2.137 0 0 1-.085-.104L4 11.746v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.359 4.359 0 0 1-.355-.508Zm2.328 3.25c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm-5 0c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm3.313-6.185c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path></svg></span>
                    <span>Copilot Coding Agent</span>
                  </div>
                </td>
                <td class="hide-mobile"><span class="type-pill cloud">Cloud</span></td>
                <td class="num">9&nbsp;375</td>
                <td class="num hide-mobile">0.34%</td>
                <td class="num hide-mobile"><span class="delta-up">▲ 3.0%</span></td>
              </tr>
              <tr style="--row-accent:#c084fc;">
                <td style="color: var(--text-muted);">3</td>
                <td>
                  <div class="agent-cell">
                    <span class="agent-logo" style="color:#c084fc"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M11.04 19.32Q12 21.51 12 24q0-2.49.93-4.68.96-2.19 2.58-3.81t3.81-2.55Q21.51 12 24 12q-2.49 0-4.68-.93a12.3 12.3 0 0 1-3.81-2.58 12.3 12.3 0 0 1-2.58-3.81Q12 2.49 12 0q0 2.49-.96 4.68-.93 2.19-2.55 3.81a12.3 12.3 0 0 1-3.81 2.58Q2.49 12 0 12q2.49 0 4.68.96 2.19.93 3.81 2.55t2.55 3.81"></path></svg></span>
                    <span>Gemini CLI</span>
                  </div>
                </td>
                <td class="hide-mobile"><span class="type-pill cli">CLI</span></td>
                <td class="num">1&nbsp;961</td>
                <td class="num hide-mobile">0.07%</td>
                <td class="num hide-mobile"><span class="delta-up">▲ 7.2%</span></td>
              </tr>
              <tr style="--row-accent:#4ade80;">
                <td style="color: var(--text-muted);">4</td>
                <td>
                  <div class="agent-cell">
                    <span class="agent-logo" style="color:#4ade80"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"></path></svg></span>
                    <span>Codex CLI</span>
                  </div>
                </td>
                <td class="hide-mobile"><span class="type-pill cli">CLI</span></td>
                <td class="num">1&nbsp;289</td>
                <td class="num hide-mobile">0.05%</td>
                <td class="num hide-mobile"><span class="delta-down">▼ -9.1%</span></td>
              </tr>
              <tr style="--row-accent:#f472b6;">
                <td style="color: var(--text-muted);">5</td>
                <td>
                  <div class="agent-cell">
                    <span class="agent-logo" style="color:#f472b6"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M23.922 16.997C23.061 18.492 18.063 22.02 12 22.02 5.937 22.02.939 18.492.078 16.997A.641.641 0 0 1 0 16.741v-2.869a.883.883 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.098 10.098 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952C7.255 2.937 9.248 1.98 11.978 1.98c2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.841.841 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256Zm-11.75-5.992h-.344a4.359 4.359 0 0 1-.355.508c-.77.947-1.918 1.492-3.508 1.492-1.725 0-2.989-.359-3.782-1.259a2.137 2.137 0 0 1-.085-.104L4 11.746v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.359 4.359 0 0 1-.355-.508Zm2.328 3.25c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm-5 0c.549 0 1 .451 1 1v2c0 .549-.451 1-1 1-.549 0-1-.451-1-1v-2c0-.549.451-1 1-1Zm3.313-6.185c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path></svg></span>
                    <span>Copilot CLI</span>
                  </div>
                </td>
                <td class="hide-mobile"><span class="type-pill cli">CLI</span></td>
                <td class="num">1&nbsp;025</td>
                <td class="num hide-mobile">0.04%</td>
                <td class="num hide-mobile"><span class="delta-up">▲ 27.0%</span></td>
              </tr>
              <tr style="--row-accent:#f59e0b;">
                <td style="color: var(--text-muted);">6</td>
                <td>
                  <div class="agent-cell">
                    <span class="agent-logo" style="color:#f59e0b"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M22.2819 9.8211a5.9847 5.9847 0 0 0-.5157-4.9108 6.0462 6.0462 0 0 0-6.5098-2.9A6.0651 6.0651 0 0 0 4.9807 4.1818a5.9847 5.9847 0 0 0-3.9977 2.9 6.0462 6.0462 0 0 0 .7427 7.0966 5.98 5.98 0 0 0 .511 4.9107 6.051 6.051 0 0 0 6.5146 2.9001A5.9847 5.9847 0 0 0 13.2599 24a6.0557 6.0557 0 0 0 5.7718-4.2058 5.9894 5.9894 0 0 0 3.9977-2.9001 6.0557 6.0557 0 0 0-.7475-7.0729zm-9.022 12.6081a4.4755 4.4755 0 0 1-2.8764-1.0408l.1419-.0804 4.7783-2.7582a.7948.7948 0 0 0 .3927-.6813v-6.7369l2.02 1.1686a.071.071 0 0 1 .038.052v5.5826a4.504 4.504 0 0 1-4.4945 4.4944zm-9.6607-4.1254a4.4708 4.4708 0 0 1-.5346-3.0137l.142.0852 4.783 2.7582a.7712.7712 0 0 0 .7806 0l5.8428-3.3685v2.3324a.0804.0804 0 0 1-.0332.0615L9.74 19.9502a4.4992 4.4992 0 0 1-6.1408-1.6464zM2.3408 7.8956a4.485 4.485 0 0 1 2.3655-1.9728V11.6a.7664.7664 0 0 0 .3879.6765l5.8144 3.3543-2.0201 1.1685a.0757.0757 0 0 1-.071 0l-4.8303-2.7865A4.504 4.504 0 0 1 2.3408 7.872zm16.5963 3.8558L13.1038 8.364 15.1192 7.2a.0757.0757 0 0 1 .071 0l4.8303 2.7913a4.4944 4.4944 0 0 1-.6765 8.1042v-5.6772a.79.79 0 0 0-.407-.667zm2.0107-3.0231l-.142-.0852-4.7735-2.7818a.7759.7759 0 0 0-.7854 0L9.409 9.2297V6.8974a.0662.0662 0 0 1 .0284-.0615l4.8303-2.7866a4.4992 4.4992 0 0 1 6.6802 4.66zM8.3065 12.863l-2.02-1.1638a.0804.0804 0 0 1-.038-.0567V6.0742a4.4992 4.4992 0 0 1 7.3757-3.4537l-.142.0805L8.704 5.459a.7948.7948 0 0 0-.3927.6813zm1.0976-2.3654l2.602-1.4998 2.6069 1.4998v2.9994l-2.5974 1.4997-2.6067-1.4997Z"></path></svg></span>
                    <span>Codex (ChatGPT)</span>
                  </div>
                </td>
                <td class="hide-mobile"><span class="type-pill cloud">Cloud</span></td>
                <td class="num">100</td>
                <td class="num hide-mobile">0.00%</td>
                <td class="num hide-mobile"><span class="delta-down">▼ -21.3%</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>`

const methodologyHtml = `
  <details>
    <summary>
      <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
      методология · источник данных — github search api
    </summary>
    <div class="body">
      Недельные счётчики коммитов получены из <a href="https://docs.github.com/en/rest/search/search#search-commits" target="_blank" rel="noopener noreferrer">GitHub Search API</a>, группировка по <code>committer-date:YYYY-MM-DD..YYYY-MM-DD</code>. Каждый агент запрашивается по тому trailer, который он фактически добавляет. Исторические (закрытые) недели замораживаются при первом успешном чтении; текущая незавершённая неделя перезапрашивается при каждом запланированном обновлении (ежедневно).
      <br><br>
      Это <strong>приблизительные значения</strong>. Search API GitHub возвращает оценки для больших результатов и помечает их флагом <code>incomplete_results: true</code>. Недельные объёмы Claude Code достаточно велики, чтобы триггерить этот флаг, но наблюдаемое расхождение между последовательными чтениями — менее 0.1%, поэтому отображаем как достоверные.
      <br><br>
      <strong>«Доля» — это доля среди отслеживаемых агентов, а не всего GitHub.</strong> 99.5% в KPI означает, что Claude Code отвечает за 99.5% недельных коммитов среди шести агентов на этом дашборде. Это <em>не</em> доля Claude Code среди всех публичных коммитов GitHub — такой знаменатель (люди + все боты) из Search API не получить; нужен GH Archive или BigQuery.
      <br><br>
      <strong>Две категории агентов.</strong> Графики конкурентов разделены по способу запуска — сравнивать терминальную утилиту и облачного агента некорректно.
      <ul>
        <li><strong>CLI-агенты</strong> работают в терминале. Вы их запускаете, они правят файлы локально, вы коммитите. <em>Claude Code, Copilot CLI, Codex CLI, Gemini CLI.</em></li>
        <li><strong>Облачные / асинхронные агенты</strong> работают как сервис. Вы ставите задачу (issue, тикет, PR-ревью), они открывают PR, когда готово. <em>Copilot Coding Agent, Codex (ChatGPT).</em></li>
      </ul>
      <strong>Учитываются (CLI-агенты):</strong>
      <ul>
        <li><strong>Claude Code</strong> — <code>Co-Authored-By: Claude &lt;noreply@anthropic.com&gt;</code></li>
        <li><strong>Copilot CLI</strong> — <code>Co-authored-by: copilot-cli</code></li>
        <li><strong>Codex CLI</strong> — <code>Co-authored-by: openai-codex</code></li>
        <li><strong>Gemini CLI</strong> — <code>Co-authored-by: gemini-cli</code></li>
      </ul>
      <strong>Учитываются (облачные / асинхронные агенты):</strong>
      <ul>
        <li><strong>Copilot Coding Agent</strong> — <code>Co-authored-by: copilot-swe-agent</code> <em>(GitHub переименовал продукт, но бот-аккаунт по-прежнему проставляет старый trailer)</em></li>
        <li><strong>Codex (ChatGPT)</strong> — <code>Co-authored-by: chatgpt-codex-connector</code></li>
      </ul>
      <strong>Каждая линия стартует с даты, когда продукт впервые стал публично доступен</strong> — research preview, public preview или open-source релиз, смотря что наступило раньше. Не GA. Выбрали именно так, потому что внедрение в превью-фазе — часть реальной истории продукта; срезать до GA — значит стереть самые интересные кривые роста.
      <br><br>
      <em>Оговорка:</em> наш backfill начинается с 5 мая 2025, раньше графика нет. Research preview Claude Code запустился 24 февраля 2025 — но его линия начинается 5 мая, потому что наши данные стартуют оттуда. Данные до мая существуют в GitHub, но не в нашем датасете. Проверенные даты запуска:
      <ul>
        <li><strong>Claude Code</strong> — <em>research preview 24 фев 2025; GA 22 мая 2025</em></li>
        <li><strong>Codex CLI</strong> — <em>open-source релиз 16 апр 2025; недельные счётчики были однозначным шумом (с выбросом в 153 коммита 5 мая из-за форк-засорения) до 28 июл 2025, когда начался устойчивый рост с 157+/нед, поэтому линия стартует оттуда, а не с запуска продукта</em></li>
        <li><strong>Codex (ChatGPT)</strong> — <em>research preview 16 мая 2025; строка trailer <code>chatgpt-codex-connector</code> появилась в коммитах только с 1 сен 2025, поэтому линия стартует оттуда, а не с запуска</em></li>
        <li><strong>Copilot Coding Agent</strong> — <em>public preview 19 мая 2025; GA 25 сен 2025</em></li>
        <li><strong>Gemini CLI</strong> — <em>open-source запуск 25 июн 2025</em></li>
        <li><strong>Copilot CLI</strong> — <em>public preview 25 сен 2025; GA 25 фев 2026</em></li>
      </ul>
      <strong>Заметка про волатильность CLI-конкурентов.</strong> Мелкие CLI-линии (Copilot CLI, Codex CLI, Gemini CLI) могут скакать от недели к неделе, когда один крупный репозиторий запускает скриптовый батч-коммит с trailer'ом агента. Дневные движения отражают репозиторный шум, а не внедрение продукта — смотрите многонедельный тренд, а не отдельные недели.
      <br><br>
      <strong>Не учитываются:</strong> Devin (чистый запрос <code>author:devin-ai-integration</code> возвращает ~92 коммита, потому что бо́льшая часть активности Devin — в приватных репо; более свободный запрос по bot-trailer засорён спам-репозиториями с поддельными trailer'ами). Windsurf / Cascade (максимум ~400 коммитов за всё время — trailer не принят). Aider, Cline / Kilo Code, CodeRabbit, Cursor, Amazon Q Developer, Jules — нет стабильного публичного trailer, который пережил бы проверки на ложноположительные срабатывания. Dependency-боты вроде Dependabot и Renovate исключены, так как обновляют зависимости, а не пишут код.
      <br><br>
      Считаются только публичные репозитории — возможен недоучёт (приватные репо, нестандартные trailer'ы) или переучёт (ложные срабатывания). <strong>Воспроизведите сами</strong> — разовый запрос по Claude Code за неделю:
      <div class="curl-box">curl -s "https://api.github.com/search/commits?q=Co-Authored-By:+Claude+noreply@anthropic.com+committer-date:2026-03-30..2026-04-05&amp;per_page=1" -H "Accept: application/vnd.github+json" -H "Authorization: token \$GITHUB_TOKEN" | jq .total_count</div>
      <br>
      Данные сэмплируются еженедельно. Вдохновлено <a href="https://aifoc.us" target="_blank" rel="noopener noreferrer">AI Focus</a> и <a href="https://semianalysis.com" target="_blank" rel="noopener noreferrer">SemiAnalysis</a>.
    </div>
  </details>`
</script>

<template>
  <div>
    <NuxtLink to="/" class="back-link-top">← советы</NuxtLink>
    <div class="terminal-window">
      <div class="title-bar">
        <div class="window-controls">
          <div class="window-control close"></div>
          <div class="window-control minimize"></div>
          <div class="window-control maximize"></div>
        </div>
        <div class="window-title">claude-cli — <span>Клодономика</span></div>
      </div>

      <div class="content">
        <div class="hero">
          <h1><span class="accent">Клодономика</span></h1>
          <p>Еженедельные коммиты от AI-агентов на публичном GitHub с момента релиза Claude Code 22&nbsp;мая&nbsp;2025 года</p>
        </div>

        <div id="dash-root" v-html="dashHtml"></div>

        <div class="methodology" id="methodology" style="display: block;" v-html="methodologyHtml"></div>

        <div class="page-footer">
          <a href="https://HowBorisUsesClaudeCode.ru" target="_blank" rel="noopener noreferrer">HowBorisUsesClaudeCode.ru</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
@import url('~/assets/css/claudeonomics.css');
</style>
