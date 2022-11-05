from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from forms import RegisterForm

app = FastAPI(title='GreenShop')

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/', response_class=HTMLResponse)
def get_main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/login', response_class=HTMLResponse)
def login_get(request: Request):
    return templates.TemplateResponse("registration.html", {"request": request})


@app.post('/login', response_class=HTMLResponse)
def login_post(request: Request, form: RegisterForm = Depends(RegisterForm.as_form)):
    context = {
        "request": request
    }
    errors = form.is_valid()
    if not errors:
        return templates.TemplateResponse("registration.html", context)
    context['errors'] = errors
    return templates.TemplateResponse("registration.html", context)


@app.get('/shop', response_class=HTMLResponse)
def shop_page(request: Request):
    context = {
        'request': request
    }

    return templates.TemplateResponse("shop.html", context)


@app.get('/card', response_class=HTMLResponse)
def card_page(request: Request):
    contex = {
        'request': request
    }

    return templates.TemplateResponse("card.html", contex)
