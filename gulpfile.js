var gulp = require('gulp'), // Подключаем Gulp
    sass = require('gulp-sass'), //Подключаем Sass пакет,
    cleanCSS = require('gulp-clean-css'), //минификация css
    rename = require('gulp-rename'),
    concat       = require('gulp-concat'),
    uglify       = require('gulp-uglifyjs'),
    autoprefixer = require('gulp-autoprefixer');// Подключаем библиотеку для автоматического добавления префиксов

gulp.task('css-2017', function () { // Создаем таск Sass
    return gulp.src(['frontend/2017/css/**/*.sass','frontend/2017/css/**/*.scss']) // Берем источник
        .pipe(sass()) // Преобразуем Sass в CSS посредством gulp-sass
        //.pipe(autoprefixer(['last 15 versions', '> 1%', 'ie 8', 'ie 7'], { cascade: true })) // Создаем префиксы
        .pipe(cleanCSS({compatibility: 'ie8'}))
        .pipe(rename({suffix: '.min'})) // Добавляем суффикс .min
        .pipe(gulp.dest('files/static/2017/css.min/')) // Выгружаем результата в папку
});

gulp.task('watch', ['css-2017'], function () {
    gulp.watch(['frontend/2017/css/**/*.sass', 'frontend/2017/css/**/*.scss'], ['css-2017']); // Наблюдение за sass файлами в папке sass
    gulp.watch(['frontend/2017/libs/**/*.js', 'frontend/2017/js/**/*.js'], ['js-2017']); // Наблюдение за sass файлами в папке sass
});

gulp.task('fonts-2017', function(){ return gulp.src('frontend/2017/fonts/**/*').pipe(gulp.dest('files/static/2017/fonts/'))});
gulp.task('icons-2017', function(){ return gulp.src('frontend/2017/icons/**/*').pipe(gulp.dest('files/static/2017/icons/'))});
gulp.task('img-2017', function(){ return gulp.src('frontend/2017/img/**/*').pipe(gulp.dest('files/static/2017/img/'))});
gulp.task('js-libs-2017', function(){ return gulp.src(['frontend/2017/libs/**/*',]).pipe(gulp.dest('files/static/2017/libs')) });
gulp.task('js-2017', function(){ return gulp.src(['frontend/2017/js/**/*.js',]).pipe(gulp.dest('files/static/2017/js/')) });

gulp.task('build-2017', ['css-2017', 'fonts-2017', 'icons-2017', 'img-2017', 'js-2017', 'js-libs-2017']);
gulp.task('default', ['watch']);