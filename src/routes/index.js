const router = require('express').Router();

router.use('/', require('./post.convert-img'));

module.exports = router;