# 🧾 REST API with Flask

This project is a simple REST API built using **Flask**, designed to perform CRUD (Create, Read, Update, Delete) operations on in-memory person data. It is intended for learning purposes and API testing using tools like **Postman**.

---

## 🚀 Features

- Add a new person using `POST`
- View all person records using `GET`
- View a specific person by index using `GET`
- Replace all data using `PUT`
- Update specific person data by index using `PUT`
- Delete specific person data by index using `DELETE`
- Delete all person data using `DELETE`
- Helpful response messages with proper status codes

---

## 📌 API Endpoints

| Method | Route                    | Description                             |
| ------ | ------------------------ | --------------------------------------- |
| GET    | `/`                      | Welcome message                         |
| GET    | `/persondetails`         | Get list of all people                  |
| GET    | `/persondetails/<index>` | Get details of a specific person        |
| POST   | `/postdata`              | Add a new person                        |
| PUT    | `/putdata`               | Replace all data with new person        |
| PUT    | `/putdata/<index>`       | Replace specific person's data by index |
| DELETE | `/deletedata/<index>`    | Delete specific person by index         |
| DELETE | `/deletedata`            | Delete all data                         |

---

## ⚙️ Requirements

Make sure you have **Python 3.7+** and **Flask** installed.

Install Flask if not already:

```bash
pip install Flask
```

---

## 💻 How to Run

1. Clone the repository or copy the code into a folder.

2. Run the app:

```bash
python app.py
```

3. Open Postman or browser to test endpoints:
   - Server runs at: `http://127.0.0.1:5000/`

---

## 📬 Example JSON for Testing

```json
{
  "name": "Rohit",
  "age": 21,
  "city": "Delhi"
}
```

---

## 🧪 Testing with Postman

You can import these requests into Postman and test the API easily:

1. Launch Postman
2. Set method (GET, POST, etc.)
3. Use the URL `http://127.0.0.1:5000/<your_route>`
4. For `POST` and `PUT`, go to **Body → raw → JSON**
5. Paste the example JSON and click **Send**

---

## Output Screenshots

#### POST Data

![Post](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754662544/Screenshot_3244_lrnme6.png)

#### GET All Persons

![Get](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754662544/Screenshot_3245_ozkffs.png)

#### GET Specific Person Data

![Get](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754662544/Screenshot_3246_fgj8fe.png)

#### PUT data

![Put](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754662544/Screenshot_3247_aiapar.png)

#### Replace specific data with PUT

![Put](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754662544/Screenshot_3248_goe6at.png)

#### Delete all Data with DELETE

![Delete](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754662545/Screenshot_3249_b2nwog.png)

#### DELETE specific data using DELETE

![Delete](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754662544/Screenshot_3252_bcfsjg.png)

---

## 📎 Notes

- This API **does not use a database**, so data resets every time the server restarts.
