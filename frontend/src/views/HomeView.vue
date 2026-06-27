<template>
  <div class="home">
    <header class="header">
      <div class="logo">Конспект Бюро</div>
      <nav class="nav">
        <a href="#about">О нас</a>
        <a href="#how-it-works">Как это работает</a>
        <a href="#pricing">Стоимость</a>
        <a href="#faq">Вопросы</a>
        <a href="#contacts">Контакты</a>
        <a href="#" @click.prevent="$router.push('/client')" class="nav-client">Мои заявки</a>
      </nav>
    </header>

    <!-- Герой -->
    <section class="hero">
      <div class="hero-content">
        <h1>Ручные конспекты <span class="highlight">на заказ</span></h1>
        <p class="hero-subtitle">
          Разборчивый почерк, любой формат, сдача точно в срок.<br>
          Вам не нужно ничего писать — мы сделаем это за вас.
        </p>
        <div class="hero-features">
          <div class="feature-item"><span class="feature-icon">✍️</span><span>Разборчивый почерк</span></div>
          <div class="feature-item"><span class="feature-icon">⚡</span><span>От 2 дней</span></div>
          <div class="feature-item"><span class="feature-icon">📄</span><span>Любой объём</span></div>
        </div>
        <button class="cta-button" @click="$router.push('/order')">Заказать конспект <span class="arrow">→</span></button>
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

    <!-- О нас -->
    <section id="about" class="about">
      <h2>Конспект Бюро — берем на себя скучную работу,<br>пока вы занимаетесь важным</h2>
      <div class="about-content">
        <p>Переписывание лекций — это рутина, которая съедает ваше личное время. Мы знаем, что иногда проще заказать эту работу, чем часами сидеть над тетрадью, особенно если почерк требует идеальной аккуратности, а преподаватель принципиален.</p>
        <p><strong>«Конспект Бюро»</strong> — это ваш сервис по быстрому и качественному переносу информации из цифрового вида в рукописный. Мы перепишем для вас любые материалы: от обычных лекций до сложных схем и таблиц.</p>
        <div class="benefits">
          <div class="benefit"><span>✅</span> Идеальная аккуратность: разборчиво и красиво</div>
          <div class="benefit"><span>✅</span> Полное соответствие: информация «один в один»</div>
          <div class="benefit"><span>✅</span> Экономия времени: вы присылаете фото — получаете готовую работу</div>
          <div class="benefit"><span>✅</span> Спасение перед сессией: срочные заказы от 2 дней</div>
        </div>
        <p class="about-footer">Ваша задача — просто прислать нам фото материалов. Остальное сделаем мы.</p>
      </div>
    </section>

    <!-- Как это работает -->
    <section id="how-it-works" class="how-it-works">
      <h2>4 простых шага до готового конспекта</h2>
      <p class="section-subtitle">Вся работа проходит онлайн, а результат получаете в пункте выдачи Wildberries.</p>
      <div class="steps-grid">
        <div class="step-card">
          <div class="step-number">01</div>
          <h3>Оформление заявки</h3>
          <p>Заполните форму, выберите тип материала и прикрепите файлы. Калькулятор рассчитает стоимость.</p>
        </div>
        <div class="step-card">
          <div class="step-number">02</div>
          <h3>Оплата</h3>
          <p>100% предоплата. Это гарантирует, что мы зарезервируем время специально для вашего заказа.</p>
        </div>
        <div class="step-card">
          <div class="step-number">03</div>
          <h3>Подтверждение</h3>
          <p>Свяжемся с вами в VK для уточнения деталей. Убедитесь, что сообщения открыты.</p>
        </div>
        <div class="step-card">
          <div class="step-number">04</div>
          <h3>Доставка</h3>
          <p>Отправим через Wildberries. Стоимость доставки 69 ₽ уже включена. Вы получите трек-код.</p>
        </div>
      </div>
    </section>

    <!-- Стоимость -->
    <section id="pricing" class="pricing">
      <h2>Как рассчитывается стоимость</h2>
      <p class="section-subtitle">Цена складывается из параметров заказа. Вы видите итог сразу, до отправки.</p>
      <div class="pricing-grid">
        <div class="pricing-card">
          <div class="pricing-icon">📄</div>
          <h3>Объём работы</h3>
          <ul><li>40 ₽ за страницу</li></ul>
          <p class="example">10 страниц = 400 ₽</p>
        </div>
        <div class="pricing-card">
          <div class="pricing-icon">📸</div>
          <h3>Тип материала</h3>
          <ul>
            <li>Документ — <strong>×1</strong></li>
            <li>Презентация — <strong>×1.2</strong></li>
            <li>Фото конспекта — <strong>×1.5</strong></li>
          </ul>
        </div>
        <div class="pricing-card">
          <div class="pricing-icon">✍️</div>
          <h3>Почерк</h3>
          <ul>
            <li>Стандарт — <strong>×1</strong></li>
            <li>Разборчивый — <strong>×1.2</strong></li>
            <li>Индивидуальный — <strong>×1.5</strong></li>
          </ul>
        </div>
        <div class="pricing-card">
          <div class="pricing-icon">⏱️</div>
          <h3>Сроки</h3>
          <ul>
            <li>6+ дней — <strong>×1</strong></li>
            <li>3–5 дней — <strong>×1.5</strong></li>
            <li>2 дня — <strong>×2</strong></li>
          </ul>
        </div>
      </div>
      <div class="pricing-extras">
        <h3>Дополнительные элементы</h3>
        <div class="extras-list">
          <span>Таблицы — <strong>+30 ₽</strong></span>
          <span>Схемы — <strong>+50 ₽</strong></span>
          <span>Рисунки — <strong>+70 ₽</strong></span>
        </div>
      </div>
      <div class="pricing-cta">
        <p>🚚 Доставка 69 ₽ включена | ✅ Тетради и канцелярия включены</p>
        <button class="cta-button" @click="$router.push('/order')">Рассчитать стоимость →</button>
      </div>
    </section>

    <!-- Что входит -->
    <section class="included">
      <h2>Что входит в стоимость?</h2>
      <div class="included-grid">
        <div class="included-card">📒 Канцелярия и материалы: тетради, бумага, ручки</div>
        <div class="included-card">✍️ Работа исполнителя: переписывание с требованиями</div>
        <div class="included-card">📦 Доставка Wildberries: 69 ₽ уже включено</div>
      </div>
      <p class="included-footer">Вам не нужно ничего докупать — вы просто получаете готовый результат!</p>
    </section>

    <!-- FAQ -->
    <section id="faq" class="faq">
      <h2>Частые вопросы</h2>
      <div class="faq-list">
        <details class="faq-item">
          <summary>Как быстро вы сможете написать конспект?</summary>
          <p>Стандартный срок — от 6 дней. Срочные заказы — от 2 дней. Точный срок зависит от объёма и загрузки.</p>
        </details>
        <details class="faq-item">
          <summary>Что делать, если качество фото плохое?</summary>
          <p>Если качество материалов слишком низкое для работы, мы свяжемся с вами в VK для уточнения.</p>
        </details>
        <details class="faq-item">
          <summary>Как происходит возврат средств?</summary>
          <p>При отмене до начала работы — 100%. После начала — за вычетом выполненной части.</p>
        </details>
        <details class="faq-item">
          <summary>Нужно ли покупать тетради?</summary>
          <p>Нет! Все материалы включены в стоимость. Мы сами подбираем качественные тетради и ручки.</p>
        </details>
      </div>
    </section>

    <!-- Контакты -->
    <section id="contacts" class="contacts">
      <h2>Контакты</h2>
      <p class="section-subtitle">Есть вопросы по заказу? Мы на связи!</p>
      <div class="contacts-grid">
        <div class="contact-card">
          <div class="contact-icon">💬</div>
          <h3>VK (быстрый ответ)</h3>
          <a href="https://vk.com/konspektps" target="_blank">vk.com/konspektps</a>
        </div>
        <div class="contact-card">
          <div class="contact-icon">📧</div>
          <h3>Email</h3>
          <a href="mailto:polinashuktueva@yandex.ru">polinashuktueva@yandex.ru</a>
        </div>
        <div class="contact-card">
          <div class="contact-icon">🕐</div>
          <h3>График работы</h3>
          <p>Пн–Вс с 10:00 до 23:00 (МСК)</p>
          <p class="contact-hint">Приём заявок — круглосуточно</p>
        </div>
      </div>
      <div class="contacts-footer">
        <p>ИП/Самозанятый: Шуктуева Полина Алексеевна</p>
        <p>ИНН: 531301882304</p>
      </div>
    </section>

    <!-- Футер -->
    <footer class="footer">
      <div class="footer-content">
        <div class="footer-logo">Конспект Бюро</div>
        <p>Ручные конспекты на заказ</p>
        <div class="footer-links">
          <router-link to="/offer">Публичная оферта</router-link>
          <router-link to="/privacy">Политика конфиденциальности</router-link>
        </div>
        <button class="cta-button footer-cta" @click="$router.push('/order')">Заказать конспект</button>
      </div>
    </footer>
  </div>
</template>

<script setup>
</script>

<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; color: #1a1a2e; background: #faf9f6; line-height: 1.6; -webkit-font-smoothing: antialiased; }
html { scroll-behavior: smooth; }
</style>

<style scoped>
.header { display: flex; justify-content: space-between; align-items: center; padding: 20px 60px; background: white; border-bottom: 1px solid #eee; position: sticky; top: 0; z-index: 100; }
.logo { font-size: 22px; font-weight: 700; }
.nav { display: flex; gap: 24px; flex-wrap: wrap; }
.nav a { text-decoration: none; color: #666; font-size: 14px; }
.nav a:hover { color: #4a67d9; }
.nav-client { color: #4a67d9 !important; font-weight: 600; }

.hero { display: flex; align-items: center; justify-content: space-between; min-height: 85vh; padding: 60px; background: linear-gradient(135deg, #f0f4ff 0%, #faf9f6 50%, #fff5f0 100%); }
.hero-content { max-width: 550px; }
.hero-content h1 { font-size: 52px; font-weight: 800; line-height: 1.2; margin-bottom: 20px; }
.highlight { color: #4a67d9; }
.hero-subtitle { font-size: 18px; color: #666; margin-bottom: 32px; }
.hero-features { display: flex; gap: 16px; margin-bottom: 36px; flex-wrap: wrap; }
.feature-item { display: flex; align-items: center; gap: 8px; background: white; padding: 10px 16px; border-radius: 30px; font-size: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); }
.cta-button { display: inline-flex; align-items: center; gap: 8px; background: #4a67d9; color: white; border: none; padding: 18px 40px; font-size: 18px; font-weight: 600; border-radius: 14px; cursor: pointer; }
.cta-button:hover { background: #3a54c0; }
.hero-hint { margin-top: 16px; font-size: 14px; color: #999; }
.hero-image { flex-shrink: 0; }
.notebook-mockup { width: 360px; height: 460px; background: white; border-radius: 8px 20px 20px 8px; box-shadow: 0 20px 60px rgba(0,0,0,0.12); position: relative; overflow: hidden; }
.notebook-page { padding: 40px 30px 40px 50px; height: 100%; }
.page-margin { position: absolute; left: 40px; top: 0; bottom: 0; width: 1px; background: #ffcccc; }
.page-lines { display: flex; flex-direction: column; gap: 20px; padding-top: 10px; }
.line { height: 2px; background: linear-gradient(90deg, #e0e0e0, #f0f0f0); border-radius: 1px; }

section { padding: 100px 60px; }
section h2 { text-align: center; font-size: 36px; margin-bottom: 20px; }
.section-subtitle { text-align: center; color: #666; font-size: 17px; margin-bottom: 50px; max-width: 600px; margin-left: auto; margin-right: auto; }

.about { background: white; }
.about-content { max-width: 800px; margin: 0 auto; font-size: 16px; color: #444; }
.about-content p { margin-bottom: 20px; }
.benefits { display: flex; flex-direction: column; gap: 12px; margin: 30px 0; }
.benefit { display: flex; align-items: center; gap: 10px; }
.about-footer { font-weight: 600; color: #1a1a2e; }

.how-it-works { background: #faf9f6; }
.steps-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; max-width: 1100px; margin: 0 auto; }
.step-card { text-align: center; padding: 40px 20px; background: white; border-radius: 20px; }
.step-number { font-size: 48px; font-weight: 800; color: #4a67d9; opacity: 0.2; margin-bottom: 12px; }
.step-card h3 { font-size: 18px; margin-bottom: 10px; }
.step-card p { color: #666; font-size: 14px; }

.pricing { background: white; }
.pricing-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; max-width: 1100px; margin: 0 auto 40px; }
.pricing-card { background: #faf9f6; padding: 30px 20px; border-radius: 16px; }
.pricing-icon { font-size: 32px; margin-bottom: 12px; }
.pricing-card h3 { font-size: 18px; margin-bottom: 12px; }
.pricing-card ul { list-style: none; margin-bottom: 10px; }
.pricing-card li { font-size: 14px; color: #555; padding: 3px 0; }
.example { font-size: 13px; color: #999; font-style: italic; border-top: 1px solid #eee; padding-top: 10px; }
.pricing-extras { text-align: center; margin-bottom: 30px; background: #faf9f6; padding: 24px; border-radius: 16px; max-width: 500px; margin-left: auto; margin-right: auto; }
.extras-list { display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 12px; }
.pricing-cta { text-align: center; }
.pricing-cta p { margin-bottom: 16px; color: #27ae60; font-weight: 600; }

.included { background: #faf9f6; }
.included-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 900px; margin: 0 auto 30px; }
.included-card { background: white; padding: 30px; border-radius: 16px; text-align: center; font-weight: 600; }
.included-footer { text-align: center; font-weight: 600; color: #27ae60; }

.faq { background: white; }
.faq-list { max-width: 700px; margin: 0 auto; }
.faq-item { border-bottom: 1px solid #eee; padding: 20px 0; cursor: pointer; }
.faq-item summary { font-size: 18px; font-weight: 600; list-style: none; display: flex; justify-content: space-between; }
.faq-item summary::after { content: '+'; font-size: 24px; color: #4a67d9; }
.faq-item[open] summary::after { content: '−'; }
.faq-item p { margin-top: 12px; color: #666; }

.contacts { background: #faf9f6; }
.contacts-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; max-width: 800px; margin: 0 auto 30px; }
.contact-card { background: white; padding: 30px; border-radius: 16px; text-align: center; }
.contact-icon { font-size: 36px; margin-bottom: 12px; }
.contact-card h3 { font-size: 17px; margin-bottom: 8px; }
.contact-card a { color: #4a67d9; text-decoration: none; font-weight: 600; }
.contact-hint { font-size: 13px; color: #999; margin-top: 6px; }
.contacts-footer { text-align: center; color: #888; font-size: 14px; }
.contacts-footer p { margin: 4px 0; }

.footer { background: #1a1a2e; color: white; text-align: center; padding: 60px; }
.footer-logo { font-size: 24px; font-weight: 700; margin-bottom: 12px; }
.footer p { color: #aaa; margin-bottom: 20px; }
.footer-links { display: flex; justify-content: center; gap: 24px; margin-bottom: 24px; }
.footer-links a { color: #aaa; text-decoration: none; font-size: 14px; }
.footer-links a:hover { color: white; }
.footer-cta { background: white; color: #1a1a2e; }
.footer-cta:hover { background: #eee; }

@media (max-width: 900px) {
  .hero { flex-direction: column; text-align: center; padding: 40px 20px; min-height: auto; }
  .hero-content h1 { font-size: 32px; }
  .header { padding: 16px 20px; }
  .nav { display: none; }
  section { padding: 60px 20px; }
  .steps-grid, .pricing-grid, .included-grid, .contacts-grid { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 500px) {
  .steps-grid, .pricing-grid, .included-grid, .contacts-grid { grid-template-columns: 1fr; }
}
</style>