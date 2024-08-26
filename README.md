# Chronicle Blogs

Chronicle Blogs is a dynamic and modern blogging web application that allows users to create, view, and manage blog posts. Built with Flask and MongoDB, this application features user authentication, rich-text editing, and image uploads. It also includes pagination, search functionality, and responsive design using Bootstrap.

## Features

- **User Authentication**: Secure registration, login, and logout functionalities.
- **Blog Posts**: Create, edit, and delete blog posts with rich-text content.
- **Pagination**: Navigate through blog posts easily with paginated views.
- **Search Functionality**: Search blog posts by title or author.
- **Responsive Design**: Fully responsive layout using Bootstrap, ensuring a seamless experience on any device.

## Installation

### Prerequisites

- Python 3.x
- Flask
- MongoDB

### Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/chronicle-blogs.git
    cd chronicle-blogs
    ```

2. **Set up environment variables:**
    ```bash
    PYTHONPATH=.
    ```

3. **Run the application:**
    ```bash
    ./web/blog.py
    ```

4. **Access the application:**
    - Open your browser and go to `http://127.0.0.1:5000`

## Usage

1. **Home Page:**
   - View recent blog posts.
   - Navigate through pages using pagination.
   - Use the search bar to find posts by title.

2. **User Account:**
   - Register or log in to create and manage your blog posts.
   - Edit your profile and update your profile picture.

3. **Create a Post:**
   - Navigate to the "New Post" page.
   - Add a title $ content.
   - Save the post to see it appear on the home page.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Micro web framework for Python.
- [MongoDB](https://www.mongodb.com/) - NoSQL database used for data storage.
- [Bootstrap](https://getbootstrap.com/) - Front-end component library for responsive design.
