const fs = require('fs');

function pseudoRandom(seed) {
  let x = Math.sin(seed) * 10000;
  return x - Math.floor(x);
}

function generateYearData({
  year,
  startMonth,
  startDay,
  endMonth,
  endDay,
  seedBase,
  targetTotal = 0,
  isZero = false
}) {
  const startYear = (startMonth > endMonth || (startMonth === endMonth && startDay >= endDay)) ? year - 1 : year;
  const startDate = new Date(Date.UTC(startYear, startMonth - 1, startDay));
  const endDate = new Date(Date.UTC(year, endMonth - 1, endDay));
  
  // Align startDate to previous Sunday
  const startDayOfWeek = startDate.getUTCDay();
  startDate.setUTCDate(startDate.getUTCDate() - startDayOfWeek);
  
  // Target exactly 53 weeks (371 days)
  const totalDaysTarget = 53 * 7;
  
  const days = [];
  let cur = new Date(startDate.getTime());
  let seed = seedBase;

  const monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];

  if (isZero) {
    for (let d = 0; d < totalDaysTarget; d++) {
      const yStr = cur.getUTCFullYear();
      const mStr = String(cur.getUTCMonth() + 1).padStart(2, '0');
      const dStr = String(cur.getUTCDate()).padStart(2, '0');
      const dateStr = `${yStr}-${mStr}-${dStr}`;
      const formatted = `${monthNames[cur.getUTCMonth()]} ${cur.getUTCDate()}, ${yStr}`;
      days.push([0, 0, dateStr, formatted]);
      cur.setUTCDate(cur.getUTCDate() + 1);
    }
  } else {
    // Generate candidates and adjust weights to match targetTotal precisely
    const rawCounts = [];
    let runningRaw = 0;
    let inStreak = false;
    let streakDays = 0;

    for (let d = 0; d < totalDaysTarget; d++) {
      const dayOfWeek = cur.getUTCDay();
      const isWeekend = (dayOfWeek === 0 || dayOfWeek === 6);

      if (streakDays > 0) {
        streakDays--;
      } else {
        inStreak = pseudoRandom(seed++) < 0.25;
        if (inStreak) streakDays = 3 + Math.floor(pseudoRandom(seed++) * 6);
      }

      const r = pseudoRandom(seed++);
      // Target active day count proportional to total
      const maxActiveDays = Math.min(260, Math.max(20, Math.round(targetTotal * 0.4)));
      const baseProb = maxActiveDays / totalDaysTarget;
      const chance = inStreak ? (isWeekend ? baseProb * 1.2 : baseProb * 1.6) : (isWeekend ? baseProb * 0.4 : baseProb);
      
      let weight = 0;
      if (r < chance) {
        const p = pseudoRandom(seed++);
        if (p < 0.55) weight = 1;
        else if (p < 0.80) weight = 2 + Math.floor(pseudoRandom(seed++) * 2);
        else if (p < 0.94) weight = 4 + Math.floor(pseudoRandom(seed++) * 3);
        else weight = 8 + Math.floor(pseudoRandom(seed++) * 6);
      }
      rawCounts.push(weight);
      runningRaw += weight;
      cur.setUTCDate(cur.getUTCDate() + 1);
    }

    // Scale to targetTotal
    const scale = runningRaw > 0 ? targetTotal / runningRaw : 0;
    cur = new Date(startDate.getTime());
    let currentSum = 0;

    for (let d = 0; d < totalDaysTarget; d++) {
      let count = 0;
      if (rawCounts[d] > 0) {
        count = Math.max(0, Math.round(rawCounts[d] * scale));
      }

      let level = 0;
      if (count >= 10) level = 4;
      else if (count >= 6) level = 3;
      else if (count >= 3) level = 2;
      else if (count >= 1) level = 1;

      const yStr = cur.getUTCFullYear();
      const mStr = String(cur.getUTCMonth() + 1).padStart(2, '0');
      const dStr = String(cur.getUTCDate()).padStart(2, '0');
      const dateStr = `${yStr}-${mStr}-${dStr}`;
      const formatted = `${monthNames[cur.getUTCMonth()]} ${cur.getUTCDate()}, ${yStr}`;

      days.push([count, level, dateStr, formatted]);
      currentSum += count;
      cur.setUTCDate(cur.getUTCDate() + 1);
    }

    // Fine-tune to hit targetTotal accurately
    let diff = targetTotal - currentSum;
    let idx = 0;
    while (diff !== 0 && idx < totalDaysTarget) {
      const day = days[idx % totalDaysTarget];
      if (diff > 0 && day[0] > 0) {
        day[0]++;
        diff--;
      } else if (diff < 0 && day[0] > 1) {
        day[0]--;
        diff++;
      }
      // Recompute level
      if (day[0] >= 10) day[1] = 4;
      else if (day[0] >= 6) day[1] = 3;
      else if (day[0] >= 3) day[1] = 2;
      else if (day[0] >= 1) day[1] = 1;
      else day[1] = 0;
      idx++;
    }
  }

  // Month labels
  const shortMonths = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  const monthLabels = [];
  for (let w = 0; w < 53; w++) {
    const weekDays = days.slice(w * 7, (w + 1) * 7);
    const firstOfMonth = weekDays.find(d => d[2].endsWith('-01'));
    if (firstOfMonth) {
      const m = parseInt(firstOfMonth[2].split('-')[1], 10) - 1;
      if (w <= 48) monthLabels.push({ col: w, label: shortMonths[m] });
    } else if (w === 0) {
      const m = parseInt(weekDays[0][2].split('-')[1], 10) - 1;
      monthLabels.push({ col: 0, label: shortMonths[m] });
    }
  }

  const finalTotal = days.reduce((sum, d) => sum + d[0], 0);
  return { total: finalTotal, monthLabels, days };
}

// User specifications:
// - 2026: 1,200 contributions
// - 2025: reduced (~780)
// - 2024: reduced (~420)
// - 2023: reduced (~190)
// - 2022: reduced (~55)
// - Before that (2021, 2020): keep 0
const realisticData = {
  '2026': generateYearData({ year: 2026, startMonth: 9, startDay: 8, endMonth: 9, endDay: 7, seedBase: 1200, targetTotal: 1200 }),
  '2025': generateYearData({ year: 2025, startMonth: 1, startDay: 1, endMonth: 12, endDay: 31, seedBase: 2500, targetTotal: 780 }),
  '2024': generateYearData({ year: 2024, startMonth: 1, startDay: 1, endMonth: 12, endDay: 31, seedBase: 3400, targetTotal: 420 }),
  '2023': generateYearData({ year: 2023, startMonth: 1, startDay: 1, endMonth: 12, endDay: 31, seedBase: 4300, targetTotal: 190 }),
  '2022': generateYearData({ year: 2022, startMonth: 1, startDay: 1, endMonth: 12, endDay: 31, seedBase: 5200, targetTotal: 55 }),
  '2021': generateYearData({ year: 2021, startMonth: 1, startDay: 1, endMonth: 12, endDay: 31, seedBase: 6100, isZero: true }),
  '2020': generateYearData({ year: 2020, startMonth: 1, startDay: 1, endMonth: 12, endDay: 31, seedBase: 7000, isZero: true })
};

Object.keys(realisticData).forEach(y => {
  console.log(`${y}: ${realisticData[y].total} contributions, ${realisticData[y].days.length} days`);
});

const path = require('path');
const rootDir = path.resolve(__dirname, '..');

fs.writeFileSync(path.join(rootDir, 'src/data/githubMultiYearData.json'), JSON.stringify(realisticData, null, 2));

const defaultDays = realisticData['2026'].days.map(d => ({
  count: d[0],
  level: d[1],
  date: d[2],
  formatted: d[3]
}));

fs.writeFileSync(path.join(rootDir, 'src/data/githubContributionsData.json'), JSON.stringify({
  total: realisticData['2026'].total,
  monthLabels: realisticData['2026'].monthLabels,
  contributions: defaultDays
}, null, 2));

console.log('SUCCESS: Generated realistic student contribution progression');
