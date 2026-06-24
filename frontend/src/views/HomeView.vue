<template>
  <div class="home">
    <!-- Шапка -->
    <header class="header">
      <div class="logo">Конспект Бюро</div>
      <nav class="nav">
        <a href="#how-it-works">Как это работает</a>
        <a href="#pricing">Стоимость</a>
        <a href="#faq">Вопросы</a>
        <a href="#" @click.prevent="$router.push('/client')" class="nav-client">Мои заявки</a>
      </nav>
    </header>

    <!-- Главный экран -->
    <section class="hero">
      <div class="hero-content">
        <h1>Ручные конспекты <span class="highlight">на заказ</span></h1>
        <p class="hero-subtitle">
          Разборчивый почерк, любой формат, сдача точно в срок.<br>
          Вам не нужно ничего писать — мы сделаем это за вас.
        </p>
        <div class="hero-features">
          <div class="feature-item">
            <span class="feature-icon">✍️</span>
            <span>Разборчивый почерк</span>
          </div>
          <div class="feature-item">
            <span class="feature-icon">⚡</span>
            <span>От 1 дня</span>
          </div>
          <div class="feature-item">
            <span class="feature-icon">📄</span>
            <span>Любой объём</span>
          </div>
        </div>
        <button class="cta-button" @click="$router.push('/order')">
          Заказать конспект
          <span class="arrow">→</span>
        </button>
        <p class="hero-hint">Заполните форму за 2 минуты и получите расчёт стоимости сразу</p>
      </div>
      <div class="hero-image">
        <div class="notebook-mockup">
          <div class="notebook-page">
            <div class="page-lines">
              <div class="line" v-for="i in 7" :key="i" :style="{ width: (80 - i * 8) + '%' }"></div>
            </div>
            <div class="page-margin"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- Как это работает -->
    <section id="how-it-works" class="how-it-works">
      <h2>Как это работает</h2>
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-number">01</div>
          <h3>Заполняете заявку</h3>
          <p>Указываете объём, формат, требования к почерку и сроки. Это займёт не больше 2 минут.</p>
        </div>
        <div class="step-card">
          <div class="step-number">02</div>
          <h3>Видите стоимость</h3>
          <p>Цена рассчитывается мгновенно. Меняйте параметры — сумма обновится автоматически.</p>
        </div>
        <div class="step-card">
          <div class="step-number">03</div>
          <h3>Получаете конспект</h3>
          <p>Мы связываемся с вами для уточнения деталей и выполняем работу точно в срок.</p>
        </div>
      </div>
    </section>

    <!-- Стоимость -->
    <section id="pricing" class="pricing">
      <h2>Как рассчитывается стоимость</h2>
      <p class="pricing-subtitle">Цена складывается из четырёх параметров. Вы видите итог сразу, до отправки заявки.</p>
      
      <div class="pricing-grid">
        <div class="pricing-card">
          <div class="pricing-icon">📄</div>
          <h3>Объём работы</h3>
          <ul>
            <li>Первая страница — <strong>500 ₽</strong></li>
            <li>Каждая следующая — <strong>150 ₽</strong></li>
          </ul>
          <p class="example">Пример: 5 страниц = 500 + (4 × 150) = 1 100 ₽</p>
        </div>
        
        <div class="pricing-card">
          <div class="pricing-icon">📒</div>
          <h3>Формат</h3>
          <ul>
            <li>Тетрадь А4 — коэффициент <strong>×1</strong></li>
            <li>Тетрадь А5 — коэффициент <strong>×0,8</strong></li>
            <li>Лист А4 — коэффициент <strong>×0,6</strong></li>
          </ul>
          <p class="example">Пример: 5 стр. в А5 = 1 100 × 0,8 = 880 ₽</p>
        </div>
        
        <div class="pricing-card">
          <div class="pricing-icon">✍️</div>
          <h3>Почерк</h3>
          <ul>
            <li>Не имеет значения — <strong>×1</strong></li>
            <li>Разборчивый — <strong>×1,2</strong></li>
            <li>Индивидуальный подбор — <strong>×1,5</strong></li>
          </ul>
          <p class="example">Пример: разборчивый = 880 × 1,2 = 1 056 ₽</p>
        </div>
        
        <div class="pricing-card">
          <div class="pricing-icon">⏱️</div>
          <h3>Сроки</h3>
          <ul>
            <li>4+ дней — <strong>×1</strong> (стандарт)</li>
            <li>2–3 дня — <strong>×1,5</strong></li>
            <li>1 день — <strong>×2</strong> (срочно)</li>
          </ul>
          <p class="example">Пример: за 2 дня = 1 056 × 1,5 = 1 584 ₽</p>
        </div>
      </div>
      
      <div class="pricing-extras">
        <h3>Дополнительные элементы</h3>
        <div class="extras-list">
          <span>Таблицы — <strong>+150 ₽</strong></span>
          <span>Схемы — <strong>+150 ₽</strong></span>
          <span>Рисунки — <strong>+200 ₽</strong></span>
          <span>Только текст — <strong>0 ₽</strong></span>
        </div>
      </div>
      
      <div class="pricing-total-example">
        <h3>Пример полного расчёта</h3>
        <div class="calculation">
          <div class="calc-row"><span>5 страниц, тетрадь А5</span><span>880 ₽</span></div>
          <div class="calc-row"><span>Разборчивый почерк</span><span>×1,2</span></div>
          <div class="calc-row"><span>Сдача за 2 дня</span><span>×1,5</span></div>
          <div class="calc-row"><span>1 таблица + 1 рисунок</span><span>+350 ₽</span></div>
          <div class="calc-divider"></div>
          <div class="calc-row total"><span>Итого</span><span>1 934 ₽</span></div>
        </div>
      </div>
      
      <div class="pricing-cta">
        <p>Цена пересчитывается автоматически при заполнении формы.</p>
        <button class="cta-button" @click="$router.push('/order')">Рассчитать свою стоимость →</button>
      </div>
    </section>

    <!-- Частые вопросы -->
    <section id="faq" class="faq">
      <h2>Частые вопросы</h2>
      <div class="faq-list">
        <details class="faq-item">
          <summary>Как быстро вы сможете написать конспект?</summary>
          <p>Стандартный срок — от 4 дней. Если нужно срочно, можем выполнить за 1–3 дня. Точный срок зависит от объёма работы и текущей загрузки.</p>
        </details>
        <details class="faq-item">
          <summary>Какой почерк вы используете?</summary>
          <p>На выбор: обычный разборчивый почерк или индивидуально подобранный под ваш стиль. Мы учитываем все пожелания.</p>
        </details>
        <details class="faq-item">
          <summary>Что делать, если у меня нет готового материала?</summary>
          <p>Ничего страшного! Просто укажите это в заявке. Мы начнём работу, как только вы предоставите исходный материал.</p>
        </details>
        <details class="faq-item">
          <summary>Можно ли заказать доставку?</summary>
          <p>Да, мы можем отправить готовый конспект почтой или курьером. Или вы можете забрать его самостоятельно.</p>
        </details>
      </div>
    </section>

    <!-- Футер -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-logo">Конспект Бюро</div>
        <p>Ручные конспекты на заказ с 2024 года</p>
        <button class="cta-button footer-cta" @click="$router.push('/order')">Заказать конспект</button>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style>
/* Глобальные стили */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  color: #1a1a2e;
  background: #faf9f6;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

html {
  scroll-behavior: smooth;
}
</style>

<style scoped>
/* Шапка */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 60px;
  background: white;
  border-bottom: 1px solid #eee;
  position: sticky;
  top: 0;
  z-index: 100;
}
.logo {
  font-size: 22px;
  font-weight: 700;
  color: #1a1a2e;
}
.nav {
  display: flex;
  gap: 32px;
}
.nav a {
  text-decoration: none;
  color: #666;
  font-size: 15px;
  transition: color 0.3s;
}
.nav a:hover {
  color: #4a67d9;
}
.nav-client {
  color: #4a67d9 !important;
  font-weight: 600;
}

/* Герой */
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 85vh;
  padding: 60px;
  background: linear-gradient(135deg, #f0f4ff 0%, #faf9f6 50%, #fff5f0 100%);
}
.hero-content {
  max-width: 550px;
}
.hero-content h1 {
  font-size: 52px;
  font-weight: 800;
  line-height: 1.2;
  margin-bottom: 20px;
  color: #1a1a2e;
}
.highlight {
  color: #4a67d9;
  position: relative;
}
.highlight::after {
  content: '';
  position: absolute;
  bottom: 4px;
  left: 0;
  width: 100%;
  height: 8px;
  background: rgba(74, 103, 217, 0.15);
  z-index: -1;
}
.hero-subtitle {
  font-size: 18px;
  color: #666;
  margin-bottom: 32px;
  line-height: 1.6;
}
.hero-features {
  display: flex;
  gap: 20px;
  margin-bottom: 36px;
  flex-wrap: wrap;
}
.feature-item {
  display: flex;
  align-items: center;
  gap: 8px;
  background: white;
  padding: 10px 16px;
  border-radius: 30px;
  font-size: 14px;
  color: #444;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.feature-icon {
  font-size: 18px;
}
.cta-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: #4a67d9;
  color: white;
  border: none;
  padding: 18px 40px;
  font-size: 18px;
  font-weight: 600;
  border-radius: 14px;
  cursor: pointer;
  transition: all 0.3s;
  text-decoration: none;
}
.cta-button:hover {
  background: #3a54c0;
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(74, 103, 217, 0.3);
}
.arrow {
  transition: transform 0.3s;
}
.cta-button:hover .arrow {
  transform: translateX(4px);
}
.hero-hint {
  margin-top: 16px;
  font-size: 14px;
  color: #999;
}

/* Мокап тетради */
.hero-image {
  flex-shrink: 0;
}
.notebook-mockup {
  width: 360px;
  height: 460px;
  background: white;
  border-radius: 8px 20px 20px 8px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.12), 0 4px 12px rgba(0,0,0,0.06);
  position: relative;
  overflow: hidden;
}
.notebook-page {
  padding: 40px 30px 40px 50px;
  height: 100%;
}
.page-margin {
  position: absolute;
  left: 40px;
  top: 0;
  bottom: 0;
  width: 1px;
  background: #ffcccc;
}
.page-lines {
  display: flex;
  flex-direction: column;
  gap: 20px;
  padding-top: 10px;
}
.line {
  height: 2px;
  background: linear-gradient(90deg, #e0e0e0, #f0f0f0);
  border-radius: 1px;
}

/* Как это работает */
.how-it-works {
  padding: 100px 60px;
  background: white;
}
.how-it-works h2 {
  text-align: center;
  font-size: 38px;
  margin-bottom: 60px;
  color: #1a1a2e;
}
.steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 30px;
  max-width: 1000px;
  margin: 0 auto;
}
.step-card {
  text-align: center;
  padding: 40px 30px;
  background: #faf9f6;
  border-radius: 20px;
  transition: transform 0.3s;
}
.step-card:hover {
  transform: translateY(-4px);
}
.step-number {
  font-size: 48px;
  font-weight: 800;
  color: #4a67d9;
  opacity: 0.2;
  margin-bottom: 16px;
}
.step-card h3 {
  font-size: 20px;
  margin-bottom: 12px;
  color: #1a1a2e;
}
.step-card p {
  color: #666;
  font-size: 15px;
}

/* Стоимость */
.pricing {
  padding: 100px 60px;
  background: #faf9f6;
}
.pricing h2 {
  text-align: center;
  font-size: 38px;
  margin-bottom: 12px;
  color: #1a1a2e;
}
.pricing-subtitle {
  text-align: center;
  color: #666;
  font-size: 17px;
  margin-bottom: 50px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}
.pricing-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  max-width: 1100px;
  margin: 0 auto 50px;
}
.pricing-card {
  background: white;
  padding: 30px 24px;
  border-radius: 16px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.pricing-icon {
  font-size: 32px;
  margin-bottom: 16px;
}
.pricing-card h3 {
  font-size: 18px;
  margin-bottom: 14px;
  color: #1a1a2e;
}
.pricing-card ul {
  list-style: none;
  margin-bottom: 14px;
}
.pricing-card li {
  font-size: 14px;
  color: #555;
  padding: 4px 0;
}
.example {
  font-size: 13px;
  color: #999;
  font-style: italic;
  border-top: 1px solid #eee;
  padding-top: 12px;
}
.pricing-extras {
  text-align: center;
  margin-bottom: 40px;
  background: white;
  padding: 30px;
  border-radius: 16px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.pricing-extras h3 {
  margin-bottom: 16px;
}
.extras-list {
  display: flex;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
  font-size: 15px;
  color: #555;
}
.pricing-total-example {
  background: white;
  padding: 30px 40px;
  border-radius: 16px;
  max-width: 500px;
  margin: 0 auto 40px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.04);
}
.pricing-total-example h3 {
  text-align: center;
  margin-bottom: 20px;
}
.calculation {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.calc-row {
  display: flex;
  justify-content: space-between;
  font-size: 15px;
  color: #555;
}
.calc-row.total {
  font-weight: 700;
  font-size: 20px;
  color: #1a1a2e;
}
.calc-divider {
  height: 1px;
  background: #eee;
  margin: 8px 0;
}
.pricing-cta {
  text-align: center;
}
.pricing-cta p {
  margin-bottom: 20px;
  color: #666;
}

/* FAQ */
.faq {
  padding: 100px 60px;
  background: white;
}
.faq h2 {
  text-align: center;
  font-size: 38px;
  margin-bottom: 50px;
}
.faq-list {
  max-width: 700px;
  margin: 0 auto;
}
.faq-item {
  border-bottom: 1px solid #eee;
  padding: 20px 0;
  cursor: pointer;
}
.faq-item summary {
  font-size: 18px;
  font-weight: 600;
  list-style: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #1a1a2e;
}
.faq-item summary::after {
  content: '+';
  font-size: 24px;
  color: #4a67d9;
  transition: transform 0.3s;
}
.faq-item[open] summary::after {
  content: '−';
  transform: rotate(180deg);
}
.faq-item p {
  margin-top: 12px;
  color: #666;
  font-size: 15px;
  line-height: 1.6;
}

/* Футер */
.footer {
  background: #1a1a2e;
  color: white;
  text-align: center;
  padding: 60px;
}
.footer-logo {
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 12px;
}
.footer p {
  color: #aaa;
  margin-bottom: 30px;
}
.footer-cta {
  background: white;
  color: #1a1a2e;
}
.footer-cta:hover {
  background: #eee;
  box-shadow: 0 8px 24px rgba(255,255,255,0.15);
}

/* Адаптивность */
@media (max-width: 900px) {
  .hero {
    flex-direction: column;
    text-align: center;
    padding: 40px 20px;
    min-height: auto;
  }
  .hero-content h1 {
    font-size: 36px;
  }
  .hero-features {
    justify-content: center;
  }
  .hero-image {
    margin-top: 40px;
  }
  .notebook-mockup {
    width: 260px;
    height: 340px;
  }
  .steps-grid,
  .pricing-grid {
    grid-template-columns: 1fr;
  }
  .header {
    padding: 16px 20px;
  }
  .nav {
    display: none;
  }
  .how-it-works,
  .pricing,
  .faq {
    padding: 60px 20px;
  }
  .pricing-grid {
    grid-template-columns: 1fr 1fr;
  }
  .extras-list {
    flex-direction: column;
    gap: 12px;
  }
}

@media (max-width: 500px) {
  .pricing-grid {
    grid-template-columns: 1fr;
  }
}
</style>