@echo off
if "%~1"=="" (
    echo Uso: setup_github_upload.bat [URL_DEL_REPOSITORIO]
    echo Ejemplo: setup_github_upload.bat https://github.com/usuario/repositorio.git
    pause
    exit /b 1
)

echo ========================================
echo  SUBIENDO A GITHUB
echo  Tecnologias Emergentes Modular
echo ========================================
echo.

echo Configurando repositorio remoto...
git remote add origin %1

echo Configurando rama principal...
git branch -M main

echo Subiendo al repositorio...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo  SUBIDA EXITOSA
    echo ========================================
    echo.
    echo Tu proyecto ha sido subido exitosamente a GitHub!
    echo Puedes verlo en: %1
) else (
    echo.
    echo ========================================
    echo  ERROR EN LA SUBIDA
    echo ========================================
    echo.
    echo Hubo un error al subir el proyecto.
    echo Verifica que la URL del repositorio sea correcta
    echo y que tengas permisos de escritura.
)

echo.
pause
