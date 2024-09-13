# Course Management System - Backend
This repository contains the backend of a Course Management System built with Django and Django Rest Framework (DRF). It is designed to handle various functionalities such as user management, student enrollment, and course management, with API support.

## Features
* **Custom User Management:** Handles registration, login, and profile management using Django's Custom User model.
  
* **Course and Student Management:** Provides endpoints for managing courses and student enrollments.

* **JWT Authentication:** Secures the API endpoints using JSON Web Tokens.

* **API Documentation:** Comprehensive API documentation available in schema.yml.

## Tech Stack
* **Django:** Backend web framework.

* **Django Rest Framework (DRF):** For building the API.

* **JWT:** For user authentication.

* **PostgreSQL:** As the database (assumed based on standard Django setup).

## Setup Instructions
1. Clone the repository:

```bash
git clone https://github.com/yourusername/course-management-system-backend.git

cd course-management-system-backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Run the development server:

```bash
python manage.py runserver
```

## Folder Structure
* **core/:** Core logic of the project.

* **students/:** Contains code related to student functionalities.

* **users/:** Manages user-related operations such as authentication and registration.

* **schema.yml:** API schema for documentation and reference.

## API Endpoints
The API includes the following key endpoints:

* **/api/users/:** User registration and management.

* **/api/students/:** Endpoints for handling student-related operations.

* **/api/courses/:** Endpoints for course management.

## Authentication
This project uses JWT for authentication. You need to obtain a token by authenticating through the login endpoint and include it in the Authorization header for protected routes.

## Contributing
Feel free to open a pull request to contribute to this project.

## License
This project is licensed under the MIT License.

--------------------------------------------------------

# Ders Yönetim Sistemi - Backend

Bu repo, Django ve Django Rest Framework (DRF) kullanılarak geliştirilmiş bir Ders Yönetim Sistemi'nin backend kısmını içerir. Kullanıcı yönetimi, öğrenci kaydı ve ders yönetimi gibi çeşitli işlevleri destekler ve API desteği sunar.

## Özellikler

* **Özel Kullanıcı Yönetimi:** Django'nun özel kullanıcı modeli kullanılarak kayıt, giriş ve profil yönetimi işlemlerini yapar.
  
* **Ders ve Öğrenci Yönetimi:** Ders ve öğrenci kayıtları için API uç noktaları sağlar.

* **JWT Kimlik Doğrulama:** API uç noktalarını JSON Web Token'ları ile güvence altına alır.

* **API Dokümantasyonu:** schema.yml dosyasında API dokümantasyonuna erişebilirsiniz.

## Teknoloji Yığını

* **Django:** Backend web framework'ü.
* **Django Rest Framework (DRF):** API oluşturmak için kullanılır.
* **JWT:** Kullanıcı kimlik doğrulaması için.
* **PostgreSQL:** Veritabanı olarak (Django'nun standart kurulumuna göre varsayılmıştır).

## Kurulum Adımları

1. Depoyu klonlayın:

```bash
git clone https://github.com/yourusername/course-management-system-backend.git

cd course-management-system-backend
```

2. Gereksinimleri yükleyin:

```bash
pip install -r requirements.txt
```

3. Veritabanı migrasyonlarını uygulayın:

```bash
python manage.py migrate
```

4. Geliştirme sunucusunu çalıştırın:

```bash
python manage.py runserver
```

## Klasör Yapısı

* **core/:** Projenin ana mantığının bulunduğu klasör.

* **students/:** Öğrencilere ait işlevselliklerin yönetildiği klasör.

* **users/:** Kullanıcılarla ilgili işlemleri (kimlik doğrulama, kayıt vb.) yöneten klasör.

* **schema.yml:** API şeması ve dokümantasyonu için kullanılan dosya.

## API Uç Noktaları

Proje şu anahtar API uç noktalarını içerir:

* **/api/users/:** Kullanıcı kayıt ve yönetim işlemleri.

* **/api/students/:** Öğrencilere yönelik işlemler.

* **/api/courses/:** Ders yönetimiyle ilgili işlemler.

## Kimlik Doğrulama

Bu proje JWT kimlik doğrulama yöntemi kullanmaktadır. Giriş yaparak bir token alabilir ve korunmuş uç noktalara erişim için bu token'ı Authorization başlığında gönderebilirsiniz.

## Katkıda Bulunma
Projeye katkıda bulunmak için pull request açabilirsiniz.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
