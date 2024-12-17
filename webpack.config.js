const path = require('path');

module.exports = {
    mode: 'production',
    entry: './node_modules/aieditor/dist/index.js',
    output: {
        path: path.resolve(__dirname, 'django_aieditor/static/django_aieditor/js'),
        filename: 'aieditor.umd.js',
        library: {
            name: 'AiEditor',
            type: 'umd',
            export: 'AiEditor'
        },
        globalObject: 'this'
    }
}; 