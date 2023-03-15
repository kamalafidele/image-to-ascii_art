const express = require('express');
const { PythonShell } = require('python-shell');
const multer = require('multer');
const fs = require('fs');

const storage = multer.diskStorage({
    destination: './uploads/',
    filename: (req, file, cb) => {
        cb(null, `image_to_convert.${file.originalname.split('.')[1]}`)
    }
})

const upload = multer({ storage });
const router = express.Router();

router.post(
  '/convert-img-to-ascii',
  upload.single('file'),
  async (req, res, next) => {

    const { file } = req;

    try {        

        const ascii_art = await PythonShell.run('app.py', null);
        fs.unlinkSync(file.path);

        console.log(ascii_art);
        return res.status(200).json({ ascii_art });
    } catch (e) {
        return res.status(500).json(e);
    }
  }
);

module.exports = router;
