
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "How Boris Uses Claude Code",
      "url": "https://howborisusesclaudecode.com",
      "description": "79 tips from the creator of Claude Code on how he uses it daily",
      "about": {
        "@type": "SoftwareApplication",
        "name": "Claude Code",
        "applicationCategory": "DeveloperApplication",
        "operatingSystem": "macOS, Linux",
        "author": { "@type": "Organization", "name": "Anthropic" }
      }
    }
    
/* --- */

        let currentVolume = 1;
        const volumeMaxTabs = { 1: 13, 2: 10, 3: 12, 4: 5, 5: 2, 6: 3, 7: 8, 8: 0, 9: 0, 10: 4, 11: 15, 12: 7 };

        function copyToClipboard(text, button) {
            navigator.clipboard.writeText(text).then(() => {
                const originalText = button.textContent;
                button.textContent = 'copied!';
                button.style.color = 'var(--green-success)';
                setTimeout(() => {
                    button.textContent = originalText;
                    button.style.color = 'var(--text-secondary)';
                }, 2000);
            });
        }

        function formatLargeNumber(n) {
            if (n >= 1_000_000) return (Math.floor(n / 100_000) / 10).toFixed(1) + 'M+';
            if (n >= 1_000) return (Math.floor(n / 100) / 10).toFixed(1) + 'K+';
            return n.toLocaleString();
        }

        // Growth chart using Netlify Functions
        async function fetchAndRenderChart() {
            window.siteStats = {};

            try {
                const data = await fetch('/api/history').then(r => r.json());
                if (data && data.count > 0) {
                    renderGrowthChart(data);
                    document.getElementById('growth-chart-wrapper').style.display = 'block';
                    window.siteStats.installs = data.count;
                    document.getElementById('social-card-wrapper').style.display = 'block';
                }
            } catch (e) {
                // History API unavailable — chart stays hidden.
            }
        }

        function renderGrowthChart(data) {
            const { count, history } = data;
            const chartLine = document.getElementById('chart-line');
            const chartArea = document.getElementById('chart-area');
            const endpoint = document.getElementById('chart-endpoint');

            // Update total count
            document.getElementById('chart-total-count').textContent = count.toLocaleString();

            // Chart dimensions
            const width = 468;
            const height = 120;
            const padding = { top: 10, bottom: 10, left: 0, right: 8 };
            const chartWidth = width - padding.left - padding.right;
            const chartHeight = height - padding.top - padding.bottom;

            // If no history, show a simple rising line from 0 to current count
            if (!history || history.length === 0) {
                document.getElementById('chart-time-start').textContent = 'start';

                // Simple diagonal line from bottom-left to top-right
                const startY = height - padding.bottom;
                const endY = padding.top + 10; // near top
                const endX = width - padding.right;

                const linePath = `M ${padding.left} ${startY} L ${endX} ${endY}`;
                chartLine.setAttribute('d', linePath);

                const areaPath = `${linePath} L ${endX} ${height - padding.bottom} L ${padding.left} ${height - padding.bottom} Z`;
                chartArea.setAttribute('d', areaPath);

                endpoint.setAttribute('cx', endX);
                endpoint.setAttribute('cy', endY);
                endpoint.style.display = 'block';
                return;
            }

            // Fixed time window: start from Feb 3, 2026 6:00 AM PST (launch time)
            // This gives a consistent baseline showing growth from launch
            const launchTime = new Date('2026-02-03T06:00:00-08:00').getTime();
            const maxTime = Date.now();
            const minTime = launchTime;
            const timeRange = maxTime - minTime;

            // Update time labels - show launch date
            document.getElementById('chart-time-start').textContent = 'Feb 3';

            // Calculate points - use max cumulative from history for scaling
            const maxCumulative = Math.max(count, ...history.map(h => h.cumulative));
            const points = [];

            // Add starting point at 0
            points.push({ x: padding.left, y: height - padding.bottom });

            history.forEach((h) => {
                const x = padding.left + ((h.time - minTime) / timeRange) * chartWidth;
                const y = padding.top + chartHeight - (h.cumulative / maxCumulative) * chartHeight;
                points.push({ x, y });
            });

            // Extend line to current time at final cumulative value
            const finalY = padding.top + chartHeight - (history[history.length - 1].cumulative / maxCumulative) * chartHeight;
            points.push({ x: width - padding.right, y: finalY });

            // Build line path
            let linePath = `M ${points[0].x} ${points[0].y}`;
            for (let i = 1; i < points.length; i++) {
                linePath += ` L ${points[i].x} ${points[i].y}`;
            }
            chartLine.setAttribute('d', linePath);

            // Build area path (close the shape)
            let areaPath = linePath;
            areaPath += ` L ${width - padding.right} ${height - padding.bottom}`;
            areaPath += ` L ${padding.left} ${height - padding.bottom}`;
            areaPath += ' Z';
            chartArea.setAttribute('d', areaPath);

            // Position endpoint
            const lastPoint = points[points.length - 1];
            endpoint.setAttribute('cx', lastPoint.x);
            endpoint.setAttribute('cy', lastPoint.y);
            endpoint.style.display = 'block';

            // Store data for hover interaction
            window.chartData = {
                count: count,
                history: history,
                points: points,
                minTime: minTime,
                maxTime: maxTime,
                width: width,
                height: height,
                padding: padding
            };

            // Set up hover interaction
            setupChartHover();
        }

        function setupChartHover() {
            const overlay = document.getElementById('chart-overlay');
            const tooltip = document.getElementById('chart-tooltip');
            const hoverLine = document.getElementById('chart-hover-line');
            const hoverDot = document.getElementById('chart-hover-dot');
            const svg = document.getElementById('growth-chart-svg');
            const chartBox = document.getElementById('growth-chart-wrapper').querySelector('.growth-chart-box');

            if (!overlay || !window.chartData) return;

            overlay.addEventListener('mousemove', (e) => {
                const rect = svg.getBoundingClientRect();
                const scaleX = 468 / rect.width;
                const mouseX = (e.clientX - rect.left) * scaleX;

                const { count, history, minTime, maxTime, width, height, padding } = window.chartData;
                if (!history || history.length === 0) return;

                // Find time at mouse position
                const timeRange = maxTime - minTime;
                const mouseTime = minTime + (mouseX / width) * timeRange;

                // Find the data point at or before this time
                let pointIndex = 0;
                for (let i = 0; i < history.length; i++) {
                    if (history[i].time <= mouseTime) {
                        pointIndex = i;
                    } else {
                        break;
                    }
                }

                const dataPoint = history[pointIndex];
                // If past last history point, show total count
                const lastHistoryTime = history[history.length - 1].time;
                const cumulative = mouseTime >= lastHistoryTime ? count : (dataPoint ? dataPoint.cumulative : 0);
                const pointTime = mouseTime >= lastHistoryTime ? lastHistoryTime : (dataPoint ? dataPoint.time : minTime);

                // Calculate Y position using the displayed cumulative (capped at count)
                const maxCumulative = Math.max(count, history[history.length - 1].cumulative);
                const chartHeight = height - padding.top - padding.bottom;
                const y = padding.top + chartHeight - (cumulative / maxCumulative) * chartHeight;

                // Update hover elements
                hoverLine.setAttribute('x1', mouseX);
                hoverLine.setAttribute('x2', mouseX);
                hoverLine.setAttribute('y1', y);
                hoverLine.setAttribute('y2', height);
                hoverLine.style.opacity = '1';

                hoverDot.setAttribute('cx', mouseX);
                hoverDot.setAttribute('cy', y);
                hoverDot.style.opacity = '1';

                // Update tooltip
                document.getElementById('tooltip-count').textContent = cumulative;
                const date = new Date(pointTime);
                const timeStr = date.toLocaleString('en-US', { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', hour12: true });
                document.getElementById('tooltip-time').textContent = timeStr;

                // Position tooltip centered above the dot
                const dotScreenX = (mouseX / 468) * rect.width;
                const dotScreenY = (y / 120) * rect.height;
                const tw = tooltip.offsetWidth;
                const th = tooltip.offsetHeight;
                const boxRect = chartBox.getBoundingClientRect();
                const svgLeft = rect.left - boxRect.left;
                let tx = svgLeft + dotScreenX - tw / 2;
                tx = Math.max(4, Math.min(tx, chartBox.offsetWidth - tw - 4));
                tooltip.style.left = tx + 'px';
                tooltip.style.top = Math.max(-th - 20, dotScreenY - th - 12) + 'px';
                tooltip.classList.add('visible');
            });

            overlay.addEventListener('mouseleave', () => {
                hoverLine.style.opacity = '0';
                hoverDot.style.opacity = '0';
                tooltip.classList.remove('visible');
            });
        }

        function downloadSocialCard() {
            const canvas = document.createElement('canvas');
            canvas.width = 1200;
            canvas.height = 630;
            const ctx = canvas.getContext('2d');
            const stats = window.siteStats || {};
            const mono = 'ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace';
            const sans = '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif';

            // Background
            ctx.fillStyle = '#111111';
            ctx.fillRect(0, 0, 1200, 630);

            // Orange accent line at top
            ctx.fillStyle = '#E07A41';
            ctx.fillRect(0, 0, 1200, 4);

            // Title
            ctx.fillStyle = '#E0E0E0';
            ctx.font = `700 48px ${sans}`;
            ctx.fillText('How Boris Uses Claude Code', 80, 100);

            // Subtitle
            ctx.fillStyle = '#555555';
            ctx.font = `400 22px ${sans}`;
            ctx.fillText('79 tips for Claude Code power users', 80, 145);

            // Thin separator
            ctx.fillStyle = '#2a2a2a';
            ctx.fillRect(80, 175, 1040, 1);

            // Hero stat — installs
            if (stats.installs) {
                ctx.fillStyle = '#E07A41';
                ctx.font = `700 110px ${sans}`;
                ctx.fillText(stats.installs.toLocaleString(), 80, 310);
                ctx.fillStyle = '#777777';
                ctx.font = `400 24px ${sans}`;
                ctx.fillText('skill installs', 80, 355);
            }

            // Bottom bar
            ctx.fillStyle = '#1a1a1a';
            ctx.fillRect(0, 560, 1200, 70);
            ctx.fillStyle = '#2a2a2a';
            ctx.fillRect(0, 560, 1200, 1);

            // URL
            ctx.fillStyle = '#E07A41';
            ctx.font = `500 20px ${mono}`;
            ctx.fillText('howborisusesclaudecode.com', 80, 600);

            // As-of date
            ctx.fillStyle = '#555555';
            ctx.font = `400 18px ${sans}`;
            ctx.textAlign = 'right';
            const asOf = new Date();
            ctx.fillText('as of ' + asOf.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }), 1120, 600);
            ctx.textAlign = 'left';

            canvas.toBlob(blob => {
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'how-boris-uses-claude-code.png';
                a.click();
                URL.revokeObjectURL(url);
            });
        }

        function copyInstallCommand(button) {
            const command = 'mkdir -p ~/.claude/skills/boris && curl -L -o ~/.claude/skills/boris/SKILL.md https://howborisusesclaudecode.com/api/install';
            navigator.clipboard.writeText(command).then(() => {
                button.textContent = 'copied!';
                button.style.color = 'var(--green-success)';
                button.style.borderColor = 'var(--green-success)';
                setTimeout(() => {
                    button.textContent = 'copy';
                    button.style.color = 'var(--text-secondary)';
                    button.style.borderColor = 'var(--border-color)';
                }, 2000);
            });
        }

        async function fetchThariqCount() {
            try {
                const res = await fetch('/api/history-thariq');
                const data = await res.json();
                if (data.count > 0) {
                    renderThariqChart(data);
                    document.getElementById('thariq-chart-wrapper').style.display = 'block';
                }
            } catch (e) {
                // silent fail
            }
        }

        function renderThariqChart(data) {
            const { count, history } = data;
            const chartLine = document.getElementById('thariq-chart-line');
            const chartArea = document.getElementById('thariq-chart-area');
            const endpoint = document.getElementById('thariq-chart-endpoint');

            document.getElementById('thariq-chart-total-count').textContent = count.toLocaleString();

            const width = 468;
            const height = 120;
            const padding = { top: 10, bottom: 10, left: 0, right: 8 };
            const chartWidth = width - padding.left - padding.right;
            const chartHeight = height - padding.top - padding.bottom;

            if (!history || history.length === 0) {
                document.getElementById('thariq-chart-time-start').textContent = 'start';
                const startY = height - padding.bottom;
                const endY = padding.top + 10;
                const endX = width - padding.right;
                const linePath = `M ${padding.left} ${startY} L ${endX} ${endY}`;
                chartLine.setAttribute('d', linePath);
                chartArea.setAttribute('d', `${linePath} L ${endX} ${height - padding.bottom} L ${padding.left} ${height - padding.bottom} Z`);
                endpoint.setAttribute('cx', endX);
                endpoint.setAttribute('cy', endY);
                endpoint.style.display = 'block';
                return;
            }

            // Exact same approach as boris chart
            const launchTime = new Date('2026-03-17T12:00:00-07:00').getTime();
            const maxTime = Date.now();
            const minTime = launchTime;
            const timeRange = maxTime - minTime;

            document.getElementById('thariq-chart-time-start').textContent = 'Mar 17';

            const maxCumulative = Math.max(count, ...history.map(h => h.cumulative));
            const points = [];

            // Start at 0
            points.push({ x: padding.left, y: height - padding.bottom });

            history.forEach((h) => {
                const x = padding.left + ((h.time - minTime) / timeRange) * chartWidth;
                const y = padding.top + chartHeight - (h.cumulative / maxCumulative) * chartHeight;
                points.push({ x, y });
            });

            // Extend line to right edge at final cumulative value
            const finalY = padding.top + chartHeight - (history[history.length - 1].cumulative / maxCumulative) * chartHeight;
            points.push({ x: width - padding.right, y: finalY });

            // Build line path
            let linePath = `M ${points[0].x} ${points[0].y}`;
            for (let i = 1; i < points.length; i++) {
                linePath += ` L ${points[i].x} ${points[i].y}`;
            }
            chartLine.setAttribute('d', linePath);

            // Build area path
            let areaPath = linePath;
            areaPath += ` L ${width - padding.right} ${height - padding.bottom}`;
            areaPath += ` L ${padding.left} ${height - padding.bottom}`;
            areaPath += ' Z';
            chartArea.setAttribute('d', areaPath);

            // Position endpoint
            const lastPoint = points[points.length - 1];
            endpoint.setAttribute('cx', lastPoint.x);
            endpoint.setAttribute('cy', lastPoint.y);
            endpoint.style.display = 'block';

            // Store data for hover interaction (same structure as boris chart)
            window.thariqChartData = {
                count: count,
                history: history,
                points: points,
                minTime: minTime,
                maxTime: maxTime,
                width: width,
                height: height,
                padding: padding
            };
            setupThariqChartHover();
        }

        function setupThariqChartHover() {
            const overlay = document.getElementById('thariq-chart-overlay');
            const tooltip = document.getElementById('thariq-tooltip');
            const hoverLine = document.getElementById('thariq-hover-line');
            const hoverDot = document.getElementById('thariq-hover-dot');
            const svg = document.getElementById('thariq-chart-svg');
            const chartBox = svg.closest('.growth-chart-box');

            if (!overlay || !window.thariqChartData) return;

            overlay.addEventListener('mousemove', (e) => {
                const rect = svg.getBoundingClientRect();
                const scaleX = 468 / rect.width;
                const mouseX = (e.clientX - rect.left) * scaleX;

                const { history, points, minTime, maxTime, width, height, padding } = window.thariqChartData;
                if (!points || points.length < 2) return;

                // Interpolate Y along the rendered line so dot rides the line exactly
                let y = points[points.length - 1].y;
                for (let i = 1; i < points.length; i++) {
                    if (mouseX <= points[i].x) {
                        const prev = points[i - 1];
                        const curr = points[i];
                        const dx = curr.x - prev.x;
                        const t = dx === 0 ? 0 : (mouseX - prev.x) / dx;
                        y = prev.y + t * (curr.y - prev.y);
                        break;
                    }
                }

                // Find closest data point for tooltip text
                const timeRange = maxTime - minTime;
                const mouseTime = minTime + (mouseX / width) * timeRange;
                let cumulative = 0;
                let pointTime = mouseTime;
                for (let i = 0; i < history.length; i++) {
                    if (history[i].time <= mouseTime) {
                        cumulative = history[i].cumulative;
                        pointTime = history[i].time;
                    } else {
                        break;
                    }
                }

                hoverLine.setAttribute('x1', mouseX);
                hoverLine.setAttribute('x2', mouseX);
                hoverLine.setAttribute('y1', y);
                hoverLine.setAttribute('y2', height);
                hoverLine.style.opacity = '1';

                hoverDot.setAttribute('cx', mouseX);
                hoverDot.setAttribute('cy', y);
                hoverDot.style.opacity = '1';

                document.getElementById('thariq-tooltip-count').textContent = cumulative;
                const date = new Date(pointTime);
                const timeStr = date.toLocaleString('en-US', { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit', hour12: true });
                document.getElementById('thariq-tooltip-time').textContent = timeStr;

                // Position tooltip centered above the dot
                const dotScreenX = (mouseX / 468) * rect.width;
                const dotScreenY = (y / 120) * rect.height;
                const tw = tooltip.offsetWidth;
                const th = tooltip.offsetHeight;
                const boxRect = chartBox.getBoundingClientRect();
                const svgLeft = rect.left - boxRect.left;
                let tx = svgLeft + dotScreenX - tw / 2;
                tx = Math.max(4, Math.min(tx, chartBox.offsetWidth - tw - 4));
                tooltip.style.left = tx + 'px';
                tooltip.style.top = Math.max(-th - 20, dotScreenY - th - 12) + 'px';
                tooltip.classList.add('visible');
            });

            overlay.addEventListener('mouseleave', () => {
                hoverLine.style.opacity = '0';
                hoverDot.style.opacity = '0';
                tooltip.classList.remove('visible');
            });
        }

        function copyThariqInstall(button) {
            const command = 'mkdir -p ~/.claude/skills/thariq-skills && curl -L -o ~/.claude/skills/thariq-skills/SKILL.md https://howborisusesclaudecode.com/api/install-thariq';
            navigator.clipboard.writeText(command).then(() => {
                button.textContent = 'copied!';
                button.style.color = 'var(--green-success)';
                button.style.borderColor = 'var(--green-success)';
                setTimeout(() => {
                    button.textContent = 'copy';
                    button.style.color = 'var(--text-secondary)';
                    button.style.borderColor = 'var(--border-color)';
                }, 2000);
            });
        }

        // Fetch chart when install tab is shown
        function onInstallTabShown() {
            fetchAndRenderChart();
        }

        function switchVolume(volume) {
            currentVolume = volume;

            // Update volume buttons
            document.querySelectorAll('.volume-btn').forEach(btn => {
                btn.classList.remove('active');
                if (parseInt(btn.dataset.volume) === volume) {
                    btn.classList.add('active');
                }
            });

            // Update tab bars
            document.querySelectorAll('.tab-bar[data-volume]').forEach(bar => {
                bar.classList.remove('active');
                if (parseInt(bar.dataset.volume) === volume) {
                    bar.classList.add('active');
                }
            });

            // Update content areas
            document.querySelectorAll('.content-area[data-volume]').forEach(area => {
                area.classList.remove('active');
                if (parseInt(area.dataset.volume) === volume) {
                    area.classList.add('active');
                }
            });

            // Reset to intro tab
            switchTab(0);

            // Fetch chart data when showing install tab
            if (volume === 8) {
                fetchAndRenderChart();
            }

            // Fetch thariq install count when showing skills guide tab
            if (volume === 9) {
                fetchThariqCount();
            }
        }

        function switchTab(index) {
            // Get active tab bar and content area for current volume
            const activeTabBar = document.querySelector(`.tab-bar[data-volume="${currentVolume}"]`);
            const activeContentArea = document.querySelector(`.content-area[data-volume="${currentVolume}"]`);

            // Update tabs within current volume
            activeTabBar.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
                if (parseInt(tab.dataset.tab) === index) {
                    tab.classList.add('active');
                }
            });

            // Update content within current volume
            activeContentArea.querySelectorAll('.tab-content').forEach(content => {
                content.classList.remove('active');
                if (parseInt(content.dataset.content) === index) {
                    content.classList.add('active');
                }
            });

            // Scroll tab into view on mobile
            const activeTab = activeTabBar.querySelector(`.tab[data-tab="${index}"]`);
            if (activeTab) {
                activeTab.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            }

            // Update progress indicator
            const progress = document.getElementById('progress-indicator');
            if (index === 0) {
                progress.textContent = '';
            } else {
                progress.textContent = `${index}/${volumeMaxTabs[currentVolume]}`;
            }
        }

        // Volume button click handlers
        document.querySelectorAll('.volume-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                switchVolume(parseInt(btn.dataset.volume));
            });
        });

        // Tab click handlers for both volumes
        document.querySelectorAll('.tab-bar[data-volume]').forEach(bar => {
            bar.querySelectorAll('.tab').forEach(tab => {
                tab.addEventListener('click', () => {
                    switchTab(parseInt(tab.dataset.tab));
                });
            });
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            const activeTabBar = document.querySelector(`.tab-bar[data-volume="${currentVolume}"]`);
            const activeTab = activeTabBar.querySelector('.tab.active');
            const currentIndex = parseInt(activeTab.dataset.tab);
            const maxTabs = volumeMaxTabs[currentVolume];

            if (e.key === 'ArrowRight' && currentIndex < maxTabs) {
                switchTab(currentIndex + 1);
            } else if (e.key === 'ArrowLeft' && currentIndex > 0) {
                switchTab(currentIndex - 1);
            } else if (e.key === 'Escape') {
                document.getElementById('about-modal').style.display = 'none';
            }
        });

        // 🥚 Easter egg for the curious devs
        console.log(`
%c┌─────────────────────────────────────────────────────┐
│                                                     │
│  claude-cli $ checking if you're a real dev...      │
│                                                     │
│  ✓ Console open detected                            │
│  ✓ Curiosity confirmed                              │
│  ✓ Touch grass reminder scheduled                   │
│                                                     │
│  You found the easter egg!                          │
│  Built by @CarolinaCherry with Claude Code.         │
│                                                     │
│  Time to build: 7 minutes                           │
│  Times Claude said "I'll help you with that": 847   │
│                                                     │
│  github.com/carolinacherry                          │
│                                                     │
└─────────────────────────────────────────────────────┘
`, 'color: #E07A41; font-family: monospace; font-size: 12px;');
    