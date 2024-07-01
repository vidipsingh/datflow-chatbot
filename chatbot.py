{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: flask in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (2.2.5)\n",
      "Requirement already satisfied: Werkzeug>=2.2.2 in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from flask) (2.2.3)\n",
      "Requirement already satisfied: Jinja2>=3.0 in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from flask) (3.1.3)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from flask) (2.0.1)\n",
      "Requirement already satisfied: click>=8.0 in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from flask) (8.1.7)\n",
      "Requirement already satisfied: colorama in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from click>=8.0->flask) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from Jinja2>=3.0->flask) (2.1.3)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install flask\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: Could not find a version that satisfies the requirement sqlite3 (from versions: none)\n",
      "ERROR: No matching distribution found for sqlite3\n"
     ]
    }
   ],
   "source": [
    "pip install sqlite3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: nltk in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (3.8.1)\n",
      "Requirement already satisfied: click in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from nltk) (8.1.7)\n",
      "Requirement already satisfied: joblib in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from nltk) (1.2.0)\n",
      "Requirement already satisfied: regex>=2021.8.3 in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from nltk) (2023.10.3)\n",
      "Requirement already satisfied: tqdm in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from nltk) (4.66.4)\n",
      "Requirement already satisfied: colorama in c:\\users\\kahn0\\anaconda3\\lib\\site-packages (from click->nltk) (0.4.6)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "[2024-07-01 13:02:47,983] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 2529, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1825, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1823, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "         ^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\flask\\app.py\", line 1799, in dispatch_request\n",
      "    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"C:\\Users\\kahn0\\AppData\\Local\\Temp\\ipykernel_11772\\613613382.py\", line 41, in home\n",
      "    return render_template(\"index.html\")\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 146, in render_template\n",
      "    template = app.jinja_env.get_or_select_template(template_name_or_list)\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 1081, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 1010, in get_template\n",
      "    return self._load_template(name, globals)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\jinja2\\environment.py\", line 969, in _load_template\n",
      "    template = self.loader.load(self, name, self.make_globals(globals))\n",
      "               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\jinja2\\loaders.py\", line 125, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 62, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n",
      "  File \"c:\\Users\\kahn0\\anaconda3\\Lib\\site-packages\\flask\\templating.py\", line 98, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [01/Jul/2024 13:02:47] \"GET / HTTP/1.1\" 500 -\n",
      "127.0.0.1 - - [01/Jul/2024 13:02:48] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    }
   ],
   "source": [
    "import sqlite3\n",
    "from flask import Flask, render_template, request\n",
    "import nltk\n",
    "from nltk.chat.util import Chat, reflections\n",
    "\n",
    "# Sample conversation pairs\n",
    "pairs = [\n",
    "    [r\"hello|hi|hey\", [\"Hello! Welcome to Company Name. How can I assist you today?\"]],\n",
    "    [r\"I have a question about my order\", [\"Sure, I can help with that. Can you please provide your order number?\"]],\n",
    "    [r\"(.*)12345(.*)\", [\"Thank you. Let me check the details for you. Your order is currently in transit. Would you like more details or help with something else?\"]],\n",
    "    [r\"more details please\", [\"Your order was placed on January 1st and is expected to be delivered by January 10th. Is there anything else I can help you with?\"]],\n",
    "    [r\"no that's all\", [\"Great! If you have any other questions, feel free to ask. Have a nice day!\"]],\n",
    "    [r\"tell me about product x\", [\"Sure! Product X is a high-quality widget that costs $99. Would you like to know more details or place an order?\"]],\n",
    "    [r\"place an order\", [\"Great! I'll need some information to complete your order.\"]],\n",
    "    [r\"my device is not working\", [\"I'm sorry to hear that. Can you describe the issue in more detail?\"]],\n",
    "    [r\"the screen is blank\", [\"Thank you for the details. Please try restarting the device. Did this solve the issue?\"]],\n",
    "    [r\"yes\", [\"I'm glad to hear that! Is there anything else I can help you with?\"]],\n",
    "    [r\"no\", [\"Thank you for contacting us. Have a great day!\"]],\n",
    "    [r\"no it didn't help\", [\"I'm sorry to hear that. I'll connect you with a human representative for further assistance.\"]],\n",
    "    [r\"is there anything else I can assist you with today?\", [\"No, that's all. Thank you for contacting Company Name. Have a great day!\"]]\n",
    "]\n",
    "\n",
    "# Create chatbot\n",
    "chatbot = Chat(pairs, reflections)\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Initialize the database connection\n",
    "def init_db():\n",
    "    conn = sqlite3.connect('orders.db')\n",
    "    c = conn.cursor()\n",
    "    c.execute('''\n",
    "              CREATE TABLE IF NOT EXISTS orders\n",
    "              (id INTEGER PRIMARY KEY, order_number TEXT, status TEXT, details TEXT)\n",
    "              ''')\n",
    "    conn.commit()\n",
    "    conn.close()\n",
    "\n",
    "@app.route(\"/\")\n",
    "def home():\n",
    "    return render_template(\"index.html\")\n",
    "\n",
    "@app.route(\"/get\", methods=[\"POST\"])\n",
    "def get_bot_response():\n",
    "    user_input = request.form[\"msg\"]\n",
    "\n",
    "    if \"order number\" in user_input:\n",
    "        conn = sqlite3.connect('orders.db')\n",
    "        c = conn.cursor()\n",
    "        c.execute(\"SELECT details FROM orders WHERE order_number=?\", (user_input.split()[-1],))\n",
    "        order_details = c.fetchone()\n",
    "        if order_details:\n",
    "            bot_response = f\"Thank you. Let me check the details for you. {order_details[0]}\"\n",
    "        else:\n",
    "            bot_response = \"Sorry, I couldn't find that order number.\"\n",
    "        conn.close()\n",
    "    else:\n",
    "        bot_response = chatbot.respond(user_input)\n",
    "    \n",
    "    return bot_response\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    init_db()\n",
    "    app.run()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
