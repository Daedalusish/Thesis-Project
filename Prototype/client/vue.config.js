const path = require('path')

// This exist to let API work in dev
module.exports = {
    outputDir: path.resolve(__dirname, '../server/public'),
    devServer : {
        proxy: {
            '/api': {
                target: 'http://localhost:5000'
            }
        }
    }
};