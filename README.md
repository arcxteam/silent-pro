# A Complete Run Sil3nt Pr0t0c0l for Incentivised Trusted Setup Cerem0ny (C0ntributi0n)

![image](https://github.com/user-attachments/assets/64fd52c6-fd6d-49cd-acb0-bb62c3641c40)
![image](https://github.com/user-attachments/assets/1754b50d-f1d8-4b7a-b70d-b649b8543654)

Silent Protocol utilizes zk-SNARKs to ensure privacy. zk-SNARKs require a trusted setup process to generate a proving key and verifying key.

---

## Here We Go...GAS 

**`Is there incentivized?` ![Confirm](https://img.shields.io/badge/confirm-yes-brightgreen)**

> [!IMPORTANT]
> **Disclaimer:**: To join the event Access is **limited to those referred by someone with existing access**. Participate in the Silent airdrop by contributing to circuits. Points are a system to track and reward your contributions to the ceremony. You earn points by participating in the ceremony and inviting others to join. We encourage you to maximize your point earnings as ... 🤫 **Start earning OGPs and claim Silent tokens rewards at TGE**. [Silent-FAQs](https://ceremony.silentprotocol.org/?ref=842976190050660352)

---

## How we do ?

- Note: Register is limited just inviting only [Join-Silent-Ceremony](https://ceremony.silentprotocol.org/?ref=842976190050660352)
- Need login with account Twitter/X and register email to get any code
- This script running for users in the list **`Queue`**
- This script auto pass **`ping`** and **`background-run`**
- VPS-server (optional) for auto 2-3 Day queue and manual you need uptime browsers tab on chrome/edge/firefox


## Requirements

- **Python** have 3.7 or latest version and modul
- **npm** have npm installed
- **Pm2** have processing manager 2 installed

## Setup Install

1. Clone this repository
   ```bash
   git clone https://github.com/arcxteam/silent-pro.git
   cd silent-pro
   ```
2. Install processing manager 2 (if not yet)
   ```bash
   npm install -g pm2
   ```
3. Fill your bearer-token at command here
    ```bash
    nano tokens.txt
    ```
  - Go the website with `CTRL+SHIFT+i` or `F12` or click mouse right, see `inspection`
  - Find on web look the captured below **Bearer token** and copied to input at `tokens.txt`
4. Run at first time
    ```bash
    python3 autoping.py
    ```
  - So, close the logs with command `CTRL+C`
5.  Run at second time with PM2
    ```bash
    pm2 start autoping.py --name silent-bot
    ```

![silent](https://github.com/user-attachments/assets/29dc0bcc-48cc-410a-bbb7-05f324ff97fd)

![image](https://github.com/user-attachments/assets/1782b7bc-cad2-4548-b4ad-89e1f5dc9623)

## Usefull Command Logs

- Status logs
   ```bash
   pm2 logs silent-bot
   ```
- Status stop/delete
   ```bash
   pm2 stop silent-bot
   ```

   ```bash
   pm2 delete silent-bot
   ```
- Status monitor
   ```bash
   pm2 monit or list
   ```

## ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
