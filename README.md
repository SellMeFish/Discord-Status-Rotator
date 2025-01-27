
# Discord Status Changer 🚀

This application is a **Discord Status Changer** developed with Python using `customtkinter` for the UI. It allows you to set, rotate, and manage custom statuses for your Discord profile seamlessly.

---

## Features ✨

- **Token Management** 🔑: Easily update and save your Discord user token.
- **Custom Statuses** 📝: Add, view, and manage multiple custom statuses.
- **Status Rotation** 🔄: Automatically rotate through your statuses at a customizable interval.
- **User-Friendly Interface** 🎨: Dark mode theme inspired by Discord's UI.
- **Secure Token Handling** 🔒: Save your token locally in a JSON file.

---

## Installation 🛠️

1. Clone the repository or download the script.
2. Install the required dependencies:
    ```bash
    pip install customtkinter requests
    ```
3. Run the script:
    ```bash
    python status.py
    ```

---

## Usage 🚀

1. **Add Your Token**: Enter your Discord user token in the token field and update it.
2. **Add Custom Statuses**: Write a status in the text field and click `Add Status`.
3. **Start Status Rotation**: Click `Start Rotation` to begin cycling through your statuses.

### Notes:
- Ensure your Discord token is valid.
- You can set the rotation interval in seconds using the interval field.
**- Make sure the Interval isnt too low so that you Discord Account isnt getting blocked by RateLimits!**

---

## Screenshots 📸

![Gui Preview](https://imgur.com/Fzt2DXJ.png)


---

## Troubleshooting ❓

- **Token Issues**: Make sure your token is correct and valid.
- **Rotation Not Starting**: Ensure you've added at least one status and updated your token.
- **Error Logs**: Check the console for detailed error messages.

---

## Contributing 🤝

Feel free to fork this project and submit pull requests. Contributions are welcome!
