<template>
  <div class="order-page">
    <header class="order-header">
      <div class="logo" @click="$router.push('/')">← На главную</div>
      <div class="steps-indicator">
        <div class="step-dot" :class="{ active: step >= 1, completed: step > 1 }">1</div>
        <div class="step-line" :class="{ active: step > 1 }"></div>
        <div class="step-dot" :class="{ active: step >= 2, completed: step > 2 }">2</div>
        <div class="step-line" :class="{ active: step > 2 }"></div>
        <div class="step-dot" :class="{ active: step >= 3 }">3</div>
      </div>
    </header>

    <div class="order-container">
      <aside class="price-sidebar">
        <div class="price-card">
          <div class="price-label">Итоговая стоимость</div>
          <div class="price-value">{{ calculatedPrice }} ₽</div>
          <div class="price-includes" v-if="step >= 2">
            <p>✅ Всё включено: тетради, канцелярия</p>
            <p>🚚 Доставка включена (69 ₽)</p>
          </div>
          <div class="price-breakdown" v-if="step >= 2">
            <div class="breakdown-item" v-if="basePrice > 0">
              <span>Базовая цена ({{ form.pages }} стр.)</span>
              <span>{{ basePrice }} ₽</span>
            </div>
            <div class="breakdown-item" v-if="form.material_type !== 'document'">
              <span>Тип материала ({{ materialTypeLabel }})</span>
              <span>×{{ materialTypeMultiplier }}</span>
            </div>
            <div class="breakdown-item" v-if="form.handwriting !== 'any'">
              <span>Почерк ({{ handwritingLabel }})</span>
              <span>×{{ handwritingMultiplier }}</span>
            </div>
            <div class="breakdown-item urgency" v-if="urgencyMultiplier > 1">
              <span>Срочность ({{ urgencyDays }} дн.)</span>
              <span>×{{ urgencyMultiplier }}</span>
            </div>
            <div class="breakdown-item" v-if="extrasTotal > 0">
              <span>Доп. элементы</span>
              <span>+{{ extrasTotal }} ₽</span>
            </div>
          </div>
          <div class="urgency-warning" v-if="urgencyMultiplier >= 2">
            ⚡ Срочный заказ — цена увеличена
          </div>
          <div class="price-hint" v-if="step < 2">
            Заполните параметры для расчёта
          </div>
        </div>
        
        <details class="pricing-info">
          <summary>Как рассчитывается стоимость?</summary>
          <div class="pricing-info-content">
            <p><strong>Объём:</strong> 40 ₽ за страницу</p>
            <p><strong>Тип материала:</strong> док-т×1, презентация×1.2, фото×1.5</p>
            <p><strong>Почерк:</strong> стандарт×1, разборчивый×1.2, индив.×1.5</p>
            <p><strong>Сроки:</strong> 6+ дн×1, 3-5 дн×1.5, 2 дн×2</p>
            <p><strong>Элементы:</strong> таблицы +30₽, схемы +50₽, рисунки +70₽</p>
            <p>🚚 Доставка 69 ₽ включена</p>
          </div>
        </details>
      </aside>

      <main class="form-area">
        <!-- Шаг 1 -->
        <div v-if="step === 1" class="form-step">
          <span class="step-badge">Шаг 1 из 3</span>
          <h2>Контакты</h2>
          <p class="step-desc">Оставьте данные для связи. Мы не передаём их третьим лицам.</p>
          
          <div class="form-group">
            <label>Ссылка ВКонтакте <span class="required">*</span></label>
            <input v-model="form.vk_link" type="url" placeholder="https://vk.com/ваш_профиль" class="input" />
            <span class="field-hint">Нужна для связи с вами</span>
          </div>
          
          <div class="form-group">
            <label>Номер телефона <span class="required">*</span></label>
            <input v-model="form.phone" type="tel" placeholder="+7 (999) 123-45-67" class="input" />
          </div>

          <div class="form-group">
            <label>Ближайший ПВЗ Wildberries <span class="required">*</span></label>
            <input v-model="form.delivery_address" type="text" placeholder="Например: г. Москва, ул. Тверская, 1" class="input" />
            <span class="field-hint">Доставка 69 ₽ уже включена в стоимость</span>
          </div>
          
          <button class="btn-primary" @click="nextStep" :disabled="!step1Valid">
            Далее → Параметры
          </button>
        </div>

        <!-- Шаг 2 -->
        <div v-if="step === 2" class="form-step">
          <span class="step-badge">Шаг 2 из 3</span>
          <h2>Параметры работы</h2>
          <p class="step-desc">От этих параметров зависит стоимость. Слева видно, как меняется цена.</p>
          
          <div class="form-group">
            <label>Тип вашего материала <span class="required">*</span></label>
            <div class="radio-cards">
              <label class="radio-card" v-for="mt in materialTypes" :key="mt.value"
                :class="{ selected: form.material_type === mt.value }">
                <input type="radio" v-model="form.material_type" :value="mt.value" />
                <span class="radio-icon">{{ mt.icon }}</span>
                <span class="radio-title">{{ mt.label }}</span>
                <span class="radio-price">{{ mt.priceLabel }}</span>
              </label>
            </div>
          </div>

          <div class="form-group">
            <label>Объём работы (страниц) <span class="required">*</span></label>
            <div class="input-with-suffix">
              <input v-model.number="form.pages" type="number" min="1" max="200" class="input" placeholder="10" />
              <span class="suffix">стр.</span>
            </div>
          </div>
          
          <div class="form-group">
            <label>Срок сдачи <span class="required">*</span></label>
            <input v-model="form.deadline" type="date" class="input" :min="minDate" />
            <div class="urgency-info" v-if="urgencyMultiplier > 1">
              <span v-if="urgencyMultiplier >= 2" class="urgency-tag hot">⚡ Срочно! ×2</span>
              <span v-else class="urgency-tag warm">🔥 Ускоренно ×1.5</span>
            </div>
          </div>
          
          <div class="form-group">
            <label>Формат <span class="required">*</span></label>
            <div class="radio-cards">
              <label class="radio-card" v-for="fmt in formats" :key="fmt.value"
                :class="{ selected: form.paper_format === fmt.value }">
                <input type="radio" v-model="form.paper_format" :value="fmt.value" />
                <span class="radio-icon">{{ fmt.icon }}</span>
                <span class="radio-title">{{ fmt.label }}</span>
              </label>
            </div>
          </div>
          
          <div class="form-group">
            <label>Требования к почерку <span class="required">*</span></label>
            <div class="radio-cards">
              <label class="radio-card" v-for="hw in handwritings" :key="hw.value"
                :class="{ selected: form.handwriting === hw.value }">
                <input type="radio" v-model="form.handwriting" :value="hw.value" />
                <span class="radio-icon">{{ hw.icon }}</span>
                <span class="radio-title">{{ hw.label }}</span>
                <span class="radio-price">{{ hw.priceLabel }}</span>
              </label>
            </div>
          </div>
          
          <div class="btn-row">
            <button class="btn-secondary" @click="prevStep">← Назад</button>
            <button class="btn-primary" @click="nextStep" :disabled="!step2Valid">
              Далее → Детали
            </button>
          </div>
        </div>

        <!-- Шаг 3 -->
        <div v-if="step === 3" class="form-step">
          <span class="step-badge">Шаг 3 из 3</span>
          <h2>Детали и подтверждение</h2>
          
          <div class="form-group">
            <label>Прикрепить материалы <span class="required">*</span></label>
            <div class="file-upload">
              <label class="file-label" :class="{ 'has-file': uploadedFiles.length }">
                <span v-if="!uploadedFiles.length">📎 Прикрепить файлы</span>
                <span v-else>📄 {{ uploadedFiles.length }} файл(ов)</span>
                <input type="file" @change="handleFileUpload" class="file-input" 
                  accept=".pdf,.doc,.docx,.jpg,.jpeg,.png,.txt" multiple />
              </label>
              <button v-if="uploadedFiles.length" @click="removeFiles" class="btn-remove-file" type="button">✕</button>
            </div>
            <span class="field-hint">PDF, Word, фото, текст (до 10 МБ каждый)</span>
          </div>

          <div class="form-group">
            <label>Дополнительные элементы</label>
            <div class="checkbox-cards">
              <label class="checkbox-card" :class="{ checked: form.has_tables }">
                <input type="checkbox" v-model="form.has_tables" />
                <span class="checkbox-icon">📊</span>
                <span>Таблицы</span>
                <span class="checkbox-price">+30 ₽</span>
              </label>
              <label class="checkbox-card" :class="{ checked: form.has_schemes }">
                <input type="checkbox" v-model="form.has_schemes" />
                <span class="checkbox-icon">📐</span>
                <span>Схемы</span>
                <span class="checkbox-price">+50 ₽</span>
              </label>
              <label class="checkbox-card" :class="{ checked: form.has_drawings }">
                <input type="checkbox" v-model="form.has_drawings" />
                <span class="checkbox-icon">🎨</span>
                <span>Рисунки</span>
                <span class="checkbox-price">+70 ₽</span>
              </label>
              <label class="checkbox-card" :class="{ checked: form.text_only }">
                <input type="checkbox" v-model="form.text_only" />
                <span class="checkbox-icon">📝</span>
                <span>Только текст</span>
                <span class="checkbox-price">0 ₽</span>
              </label>
            </div>
          </div>
          
          <div class="form-group">
            <label>Дополнительная информация</label>
            <textarea v-model="form.additional_info" rows="3" class="textarea" 
              placeholder="Особые требования. Если их нет, поставьте точку"></textarea>
          </div>

          <!-- Галочки -->
          <div class="form-group checkboxes-required">
            <label class="checkbox-required">
              <input type="checkbox" v-model="form.agree_offer" />
              <span>Я ознакомился с <router-link to="/offer" target="_blank">Публичной офертой</router-link>, <router-link to="/privacy" target="_blank">Политикой конфиденциальности</router-link> и согласен с условиями обработки данных <span class="required">*</span></span>
            </label>
            <label class="checkbox-required">
              <input type="checkbox" v-model="form.agree_data" />
              <span>Подтверждаю, что указанные мной данные (объем, параметры заказа) верны <span class="required">*</span></span>
            </label>
            <label class="checkbox-required">
              <input type="checkbox" v-model="form.agree_vk_open" />
              <span>Подтверждаю, что мои личные сообщения в VK открыты для связи, либо я напишу первым(-ой) для уточнения деталей заказа <span class="required">*</span></span>
            </label>
            <label class="checkbox-required">
              <input type="checkbox" v-model="form.agree_files_quality" />
              <span>Подтверждаю, что загруженные материалы чёткие и разборчивые для работы <span class="required">*</span></span>
            </label>
          </div>

          <!-- Итоговый блок -->
          <div class="final-summary">
            <h3>Проверьте заказ</h3>
            <div class="summary-list">
              <div class="summary-row"><span>ВК:</span><span>{{ form.vk_link || '—' }}</span></div>
              <div class="summary-row"><span>Телефон:</span><span>{{ form.phone || '—' }}</span></div>
              <div class="summary-row"><span>ПВЗ:</span><span>{{ form.delivery_address || '—' }}</span></div>
              <div class="summary-row"><span>Тип материала:</span><span>{{ materialTypeLabel }}</span></div>
              <div class="summary-row"><span>Объём:</span><span>{{ form.pages }} стр.</span></div>
              <div class="summary-row"><span>Срок:</span><span>{{ form.deadline || '—' }}</span></div>
              <div class="summary-row"><span>Формат:</span><span>{{ formatLabel }}</span></div>
              <div class="summary-row"><span>Почерк:</span><span>{{ handwritingLabel }}</span></div>
              <div class="summary-row total-row"><span>Итого (с доставкой):</span><span>{{ calculatedPrice }} ₽</span></div>
            </div>
            <p class="delivery-note">🚚 Доставка 69 ₽ включена | ✅ Тетради и канцелярия включены</p>
          </div>
          
          <div v-if="errorMessage" class="error-message">
            <span>❌</span> {{ errorMessage }}
          </div>
          
          <div class="btn-row">
            <button class="btn-secondary" @click="prevStep">← Назад</button>
            <button class="btn-primary btn-submit" @click="submitOrder" :disabled="submitting || !step3Valid">
              {{ submitting ? 'Отправка...' : 'Перейти к оплате' }}
            </button>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const API_URL = import.meta.env.VITE_API_URL || ''

const step = ref(1)
const submitting = ref(false)
const errorMessage = ref('')
const uploadedFiles = ref([])

const form = reactive({
  vk_link: '',
  phone: '',
  delivery_address: '',
  material_type: 'document',
  pages: 10,
  deadline: '',
  paper_format: 'A4_tetrad',
  handwriting: 'any',
  has_tables: false,
  has_schemes: false,
  has_drawings: false,
  text_only: false,
  additional_info: '.',
  get_type: 'delivery',
  agree_offer: false,
  agree_data: false,
  agree_vk_open: false,
  agree_files_quality: false,
})

const materialTypes = [
  { value: 'document', label: 'Электронный документ', icon: '📄', priceLabel: '×1' },
  { value: 'presentation', label: 'Презентация', icon: '📊', priceLabel: '×1.2' },
  { value: 'handwritten_photo', label: 'Фото рукописного конспекта', icon: '📸', priceLabel: '×1.5' },
]

const formats = [
  { value: 'A4_tetrad', label: 'Тетрадь А4', icon: '📒' },
  { value: 'A5_tetrad', label: 'Тетрадь А5', icon: '📔' },
]

const handwritings = [
  { value: 'any', label: 'Стандарт', icon: '✍️', priceLabel: '×1' },
  { value: 'readable', label: 'Разборчивый', icon: '✨', priceLabel: '×1.2' },
  { value: 'individual', label: 'Индивидуальный подбор', icon: '🎯', priceLabel: '×1.5' },
]

const minDate = computed(() => {
  const tomorrow = new Date()
  tomorrow.setDate(tomorrow.getDate() + 2)
  return tomorrow.toISOString().split('T')[0]
})

const step1Valid = computed(() => form.vk_link.trim() && form.phone.trim() && form.delivery_address.trim())
const step2Valid = computed(() => form.material_type && form.pages > 0 && form.pages <= 200 && form.deadline && form.paper_format && form.handwriting)
const step3Valid = computed(() => uploadedFiles.value.length > 0 && form.agree_offer && form.agree_data && form.agree_vk_open && form.agree_files_quality)

const basePrice = computed(() => form.pages <= 0 ? 0 : form.pages * 40)
const materialTypeMultiplier = computed(() => ({ 'document': 1, 'presentation': 1.2, 'handwritten_photo': 1.5 })[form.material_type] || 1)
const handwritingMultiplier = computed(() => ({ 'any': 1, 'readable': 1.2, 'individual': 1.5 })[form.handwriting] || 1)
const urgencyDays = computed(() => form.deadline ? Math.ceil((new Date(form.deadline) - new Date()) / (1000 * 60 * 60 * 24)) : 999)
const urgencyMultiplier = computed(() => urgencyDays.value <= 2 ? 2 : urgencyDays.value <= 5 ? 1.5 : 1)
const extrasTotal = computed(() => (form.has_tables ? 30 : 0) + (form.has_schemes ? 50 : 0) + (form.has_drawings ? 70 : 0))
const calculatedPrice = computed(() => Math.round(basePrice.value * materialTypeMultiplier.value * handwritingMultiplier.value * urgencyMultiplier.value + extrasTotal.value + 69))

const materialTypeLabel = computed(() => materialTypes.find(m => m.value === form.material_type)?.label || '')
const formatLabel = computed(() => formats.find(f => f.value === form.paper_format)?.label || '')
const handwritingLabel = computed(() => handwritings.find(h => h.value === form.handwriting)?.label || '')

function nextStep() { step.value++ }
function prevStep() { step.value-- }

function handleFileUpload(event) {
  const files = Array.from(event.target.files)
  const validFiles = files.filter(f => f.size <= 10 * 1024 * 1024)
  if (validFiles.length < files.length) alert('Некоторые файлы больше 10 МБ и не были добавлены.')
  uploadedFiles.value = [...uploadedFiles.value, ...validFiles]
}

function removeFiles() { uploadedFiles.value = [] }

async function submitOrder() {
  submitting.value = true
  errorMessage.value = ''

  try {
    const formData = new FormData()
    
    Object.keys(form).forEach(key => {
      if (!['agree_offer', 'agree_data', 'agree_vk_open', 'agree_files_quality'].includes(key)) {
        formData.append(key, form[key])
      }
    })
    formData.append('estimated_price', calculatedPrice.value)
    
    uploadedFiles.value.forEach(file => formData.append('uploaded_files', file))

    const response = await fetch(`${API_URL}/api/orders/create/`, {
      method: 'POST',
      body: formData,
    })
    
    const data = await response.json()
    
    if (response.ok) {
      router.push({ path: '/payment', query: { orderId: data.order_id, price: calculatedPrice.value } })
    } else {
      errorMessage.value = 'Ошибка: ' + JSON.stringify(data.errors || data)
    }
  } catch (e) {
    errorMessage.value = 'Не удалось отправить заявку.'
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
.order-page { min-height: 100vh; background: #faf9f6; }
.order-header { display: flex; justify-content: space-between; align-items: center; padding: 20px 40px; background: white; border-bottom: 1px solid #eee; }
.logo { font-size: 16px; font-weight: 600; color: #4a67d9; cursor: pointer; }
.steps-indicator { display: flex; align-items: center; gap: 0; }
.step-dot { width: 36px; height: 36px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px; background: #eee; color: #999; transition: all 0.3s; }
.step-dot.active { background: #4a67d9; color: white; }
.step-dot.completed { background: #d4edda; color: #155724; }
.step-line { width: 40px; height: 2px; background: #eee; transition: background 0.3s; }
.step-line.active { background: #4a67d9; }
.order-container { display: flex; max-width: 1200px; margin: 40px auto; gap: 30px; padding: 0 20px; }
.price-sidebar { width: 320px; flex-shrink: 0; position: sticky; top: 100px; align-self: flex-start; }
.price-card { background: white; border-radius: 16px; padding: 30px; box-shadow: 0 2px 16px rgba(0,0,0,0.06); text-align: center; margin-bottom: 16px; }
.price-label { font-size: 14px; color: #999; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; }
.price-value { font-size: 42px; font-weight: 800; color: #1a1a2e; margin-bottom: 12px; }
.price-includes { text-align: left; font-size: 13px; color: #27ae60; margin-bottom: 12px; }
.price-includes p { margin: 4px 0; }
.price-breakdown { text-align: left; border-top: 1px solid #eee; padding-top: 16px; }
.breakdown-item { display: flex; justify-content: space-between; font-size: 14px; color: #666; padding: 4px 0; }
.breakdown-item.urgency { color: #e67e22; }
.urgency-warning { background: #fff3cd; color: #856404; padding: 10px; border-radius: 8px; margin-top: 16px; font-size: 14px; font-weight: 600; }
.price-hint { color: #bbb; font-size: 14px; margin-top: 16px; }
.pricing-info { background: white; border-radius: 16px; padding: 16px 20px; box-shadow: 0 2px 16px rgba(0,0,0,0.06); cursor: pointer; }
.pricing-info summary { font-size: 14px; color: #4a67d9; font-weight: 600; list-style: none; }
.pricing-info-content { margin-top: 12px; font-size: 13px; color: #666; }
.pricing-info-content p { margin: 6px 0; }
.form-area { flex: 1; background: white; border-radius: 20px; padding: 40px; box-shadow: 0 2px 16px rgba(0,0,0,0.06); }
.form-step { animation: fadeIn 0.3s ease; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
.step-badge { display: inline-block; background: #f0f4ff; color: #4a67d9; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; margin-bottom: 16px; }
h2 { font-size: 28px; margin-bottom: 8px; color: #1a1a2e; }
.step-desc { color: #888; margin-bottom: 30px; font-size: 15px; }
.form-group { margin-bottom: 24px; }
label { display: block; margin-bottom: 8px; font-weight: 600; font-size: 15px; color: #333; }
.required { color: #e74c3c; }
.input, .textarea { width: 100%; padding: 14px 16px; border: 2px solid #e0e0e0; border-radius: 12px; font-size: 16px; transition: border 0.3s, box-shadow 0.3s; background: #fafafa; font-family: inherit; box-sizing: border-box; }
.input:focus, .textarea:focus { border-color: #4a67d9; box-shadow: 0 0 0 3px rgba(74, 103, 217, 0.1); background: white; outline: none; }
.input-with-suffix { display: flex; align-items: center; }
.input-with-suffix .input { border-radius: 12px 0 0 12px; }
.suffix { background: #eee; padding: 14px 16px; border-radius: 0 12px 12px 0; color: #666; font-weight: 600; }
.field-hint { display: block; margin-top: 6px; font-size: 13px; color: #aaa; }
.urgency-info { margin-top: 8px; }
.urgency-tag { display: inline-block; padding: 6px 14px; border-radius: 20px; font-size: 13px; font-weight: 600; }
.urgency-tag.hot { background: #ffeaea; color: #c0392b; }
.urgency-tag.warm { background: #fff3e0; color: #e67e22; }
.file-upload { display: flex; align-items: center; gap: 12px; }
.file-label { display: inline-block; padding: 14px 24px; background: #f0f4ff; border: 2px dashed #b0c4f0; border-radius: 12px; cursor: pointer; transition: all 0.3s; font-weight: 500; color: #4a67d9; text-align: center; flex: 1; }
.file-label:hover { background: #e0eaff; border-color: #4a67d9; }
.file-label.has-file { background: #eafaf1; border-color: #27ae60; border-style: solid; color: #155724; }
.file-input { display: none; }
.btn-remove-file { background: #ffeaea; color: #c0392b; border: none; width: 40px; height: 40px; border-radius: 50%; cursor: pointer; font-size: 18px; display: flex; align-items: center; justify-content: center; }
.btn-remove-file:hover { background: #fdd; }
.radio-cards, .checkbox-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 12px; }
.radio-card, .checkbox-card { display: flex; flex-direction: column; align-items: center; gap: 8px; padding: 16px 12px; border: 2px solid #e0e0e0; border-radius: 14px; cursor: pointer; transition: all 0.3s; text-align: center; }
.radio-card:hover, .checkbox-card:hover { border-color: #b0c4f0; }
.radio-card.selected, .checkbox-card.checked { border-color: #4a67d9; background: #f0f4ff; }
.radio-card input, .checkbox-card input { display: none; }
.radio-icon, .checkbox-icon { font-size: 28px; }
.radio-title, .checkbox-title { font-weight: 600; font-size: 14px; color: #333; }
.radio-price, .checkbox-price { font-size: 13px; color: #4a67d9; font-weight: 600; }
.checkboxes-required { display: flex; flex-direction: column; gap: 14px; }
.checkbox-required { display: flex; align-items: flex-start; gap: 10px; font-weight: normal !important; cursor: pointer; font-size: 14px; }
.checkbox-required input { margin-top: 3px; min-width: 18px; height: 18px; }
.checkbox-required a { color: #4a67d9; text-decoration: underline; }
.final-summary { background: #f9fafb; border-radius: 14px; padding: 24px; margin: 24px 0; }
.final-summary h3 { margin-bottom: 16px; color: #1a1a2e; }
.summary-list { display: flex; flex-direction: column; gap: 8px; }
.summary-row { display: flex; justify-content: space-between; font-size: 15px; color: #555; }
.summary-row.total-row { border-top: 1px solid #ddd; padding-top: 10px; margin-top: 4px; font-weight: 700; font-size: 18px; color: #1a1a2e; }
.delivery-note { text-align: center; color: #27ae60; font-size: 13px; margin-top: 12px; }
.btn-row { display: flex; gap: 16px; margin-top: 30px; }
.btn-primary { flex: 1; padding: 16px 28px; background: #4a67d9; color: white; border: none; border-radius: 14px; font-size: 16px; font-weight: 600; cursor: pointer; transition: all 0.3s; }
.btn-primary:hover:not(:disabled) { background: #3a54c0; }
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }
.btn-secondary { padding: 16px 28px; background: #f0f0f0; color: #555; border: none; border-radius: 14px; font-size: 16px; font-weight: 600; cursor: pointer; }
.btn-submit { background: #27ae60; }
.btn-submit:hover:not(:disabled) { background: #219a52; }
.error-message { background: #f8d7da; color: #721c24; padding: 16px 20px; border-radius: 12px; margin-top: 20px; display: flex; align-items: center; gap: 10px; }
@media (max-width: 900px) {
  .order-container { flex-direction: column; }
  .price-sidebar { width: 100%; position: static; }
  .form-area { padding: 24px; }
}
</style>