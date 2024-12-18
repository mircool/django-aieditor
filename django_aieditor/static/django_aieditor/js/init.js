// AiEditor初始化配置
window.AIEDITOR_CONFIG = window.AIEDITOR_CONFIG || {
    minHeight: '400px',
    maxHeight: '800px',
    placeholder: '请输入内容...',
    mode: 'simple',
    toolbarKeys: [
        'bold', 'italic', 'strikethrough', 'underline', 'code', '|',
        'heading', 'quote', 'unorderedList', 'orderedList', 'todoList', '|',
        'link', 'image', 'table', '|',
        'preview', 'fullscreen'
    ]
}; 

// 确保AiEditor全局可用
(function() {
    if (typeof window.AiEditor === 'undefined' && typeof require === 'function') {
        try {
            window.AiEditor = require('aieditor').AiEditor;
        } catch (e) {
            console.error('Failed to load AiEditor:', e);
        }
    }
})(); 