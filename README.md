# Tutorial-Streamit

- [Get started](https://docs.streamlit.io/en/stable/getting_started.html)
- [Tutorial: Create a data explorer app](https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html)

---

## [Get started](https://docs.streamlit.io/en/stable/getting_started.html)

### Install Streamlit

```sh
$ python -m venv myenv
$ . myenv/bin/activate
$ python -m pip install --upgrade pip
```

```sh
$ python -m pip install streamlit
$ python -m pip freeze > requirements.txt

# $ python -m pip install -r requirements.txt
```

```sh
$ streamlit hello
```

> 👋 Welcome to Streamlit!
>
> If you're one of our development partners or you're interested in getting
>
> personal technical support or Streamlit updates, please enter your email
>
> address below. Otherwise, you may leave the field blank.
>
> Email:

> Privacy Policy:
>
> As an open source project, we collect usage statistics. We cannot see and do
>
> not store information contained in Streamlit apps. You can find out more by
>
> reading our privacy policy at: https://streamlit.io/privacy-policy
>
> If you'd like to opt out of usage statistics, add the following to
>
> ~/.streamlit/config.toml, creating that file if necessary:
>
>     [browser]
>
>     gatherUsageStats = false
>
> Welcome to Streamlit. Check out our demo in your browser.
>
> Local URL: http://localhost:8501
>
> Network URL: http://192.168.179.3:8501
>
> Ready to create your own Python apps super quickly?
>
> Just head over to https://docs.streamlit.io
>
> May you create awesome apps!

### Import Streamlit

```sh
$ streamlit run first_app.py
```

### Add text and data

```sh
$ streamlit run first_app1.py
```

### Use magic

```sh
$ streamlit run first_app2.py
```

### Draw charts and maps

```sh
$ streamlit run first_app3.py
```

### Add interactivity with widgets

```sh
$ streamlit run first_app4.py
```

### Show progress

```sh
$ streamlit run first_app5.py
```

## [Tutorial: Create a data explorer app](https://docs.streamlit.io/en/stable/tutorial/create_a_data_explorer_app.html)

```sh
$ streamlit run uber_pickups.py
```
