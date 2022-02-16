# licence-key-impl

We try to build up a PoC system which include demo app and key gen app for license key verification.

### Intro
We took jwt token algorithm as the reference
![jwt_ng1_en](https://i.imgur.com/XSesjJh.png)

In our case, we use simpler way, here is the step

`[Key Generation Part]`
1. Generate random string (in our case, we use the middle of uuid4 random string)
```
ae66f1f5-ec93-4f42-a757-b8f5b939ae7e => ec93
```
2. Use SHA256 hash to generate hash string, and pick up first 12 chars, and split it with `'-'`, 
e.g. `AAAABBBBCCCC` => `AAAA-BBBB-CCCC`

3. Append upper random string `'EC93'`, and publish the license key
=> `AAAA-BBBB-CCCC-EC93`

`[Key Verification]`
For example, input license key is `AAAA-BBBB-CCCC-EC93`
1. We get last sub string `EC93`, put it lower `ec93`, it's our random string
2. Use the same algorithm to generate license key, then we will get `AAAA-BBBB-CCCC-EC93`
3. Compare with our input license key

### Example
```
(licence-key-impl-guZHDQDg-py3.6) (base) ➜  licence-key-impl git:(main) ✗ python keygen.py
Licence key generator
Your licence key: F956-0AB2-BC75-8E07
(licence-key-impl-guZHDQDg-py3.6) (base) ➜  licence-key-impl git:(main) ✗ python app.py   
Please enter you licence key: F956-0AB2-BC75-8E07
F956-0AB2-BC75-8E07
Valid license key, pass
```