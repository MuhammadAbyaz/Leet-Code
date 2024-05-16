def priceCheck(products, productPrices, productSold, soldPrice):
    product_dict = {products[i]: productPrices[i] for i in range(len(products))}
    error = 0
    for i in range(len(productSold)):
        if product_dict[productSold[i]] - soldPrice[i] != 0:
            error += 1
    return error


print(
    priceCheck(
        ["eggs", "milk", "cheese"],
        [2.89, 3.29, 5.79],
        ["eggs", "eggs", "cheese", "milk"],
        [2.89, 2.99, 5.97, 3.29],
    )
)
