# Pré-requis

* Python
* BeautifulSoup (```pip install beautifulsoup4```)
* Requests (```pip install requests```)

## Pour $noproduit = 64-137

## URL pour chercher produit

```HTML
http://cyclebabac.com/?s=64-137
```

## Code qui confirme le numéro de produit

```HTML
<span class="sku_wrapper">SKU: <span class="sku" itemprop="sku">64-137</span>.</span>
```

## Code qui retourne le nom du produit

```HTML
<h1 itemprop="name" class="product_title entry-title">Park Tool tray 106</h1>
```
