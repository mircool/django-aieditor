// AiEditor初始化配置
window.AIEDITOR_CONFIG = window.AIEDITOR_CONFIG || {
    height: '400px',
    width: '100%',
    toolbar: [
        'bold', 'italic', 'strikethrough', 'underline', 'code', '|',
        'heading', 'quote', 'unorderedList', 'orderedList', 'todoList', '|',
        'link', 'image', 'table', '|',
        'preview', 'fullscreen'
    ],
    upload: {
        url: '/upload/',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]')?.value || ''
        }
    }
}; 