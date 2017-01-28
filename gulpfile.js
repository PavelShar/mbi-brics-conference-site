var gulp = require('gulp'), // Подключаем Gulp
    sass = require('gulp-sass'), //Подключаем Sass пакет,
    cleanCSS = require('gulp-clean-css'), //минификация css
    rename = require('gulp-rename'),
    autoprefixer = require('gulp-autoprefixer');// Подключаем библиотеку для автоматического добавления префиксов

gulp.task('css-2017', function () { // Создаем таск Sass
    return gulp.src('frontend/2017/css/**/*.sass') // Берем источник
        .pipe(sass()) // Преобразуем Sass в CSS посредством gulp-sass
        //.pipe(autoprefixer(['last 15 versions', '> 1%', 'ie 8', 'ie 7'], { cascade: true })) // Создаем префиксы
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(rename({suffix: '.min'})) // Добавляем суффикс .min
        .pipe(gulp.dest('files/static/2017/css.min/')) // Выгружаем результата в папку
});

gulp.task('watch', ['css-2017'], function () {
    gulp.watch('frontend/2017/css/**/*.sass', ['css-2017']); // Наблюдение за sass файлами в папке sass
});

gulp.task('default', ['watch']);