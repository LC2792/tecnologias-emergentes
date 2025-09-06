@echo off
echo ========================================
echo  CONFIGURACION PARA GITHUB
echo  Tecnologias Emergentes Modular
echo ========================================
echo.

echo Verificando si Git esta instalado...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git no esta instalado. Por favor instala Git desde:
    echo https://git-scm.com/download/win
    echo.
    echo Despues de instalar Git, ejecuta este script nuevamente.
    pause
    exit /b 1
)

echo Git encontrado. Configurando repositorio...
echo.

echo Inicializando repositorio Git...
git init

echo Agregando archivos al repositorio...
git add .

echo Creando commit inicial...
git commit -m "Initial commit: Proyecto de Tecnologias Emergentes y Disruptivas"

echo.
echo ========================================
echo  CONFIGURACION COMPLETADA
echo ========================================
echo.
echo Para subir a GitHub:
echo 1. Ve a https://github.com y crea un nuevo repositorio
echo 2. Copia la URL del repositorio
echo 3. Ejecuta los siguientes comandos:
echo.
echo    git remote add origin [URL_DEL_REPOSITORIO]
echo    git branch -M main
echo    git push -u origin main
echo.
echo O ejecuta: setup_github_upload.bat [URL_DEL_REPOSITORIO]
echo.
pause
