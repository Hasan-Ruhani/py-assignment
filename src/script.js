document.addEventListener("DOMContentLoaded", () => {
  const hamburger = document.getElementById("hamburger");
  const mobileMenu = document.getElementById("mobile-menu");

  hamburger.addEventListener("click", () => {
    mobileMenu.classList.toggle("hidden");
  });

  // Close the mobile menu when clicking outside
  document.addEventListener("click", function (event) {
    if (
      !hamburger.contains(event.target) &&
      !mobileMenu.contains(event.target)
    ) {
      mobileMenu.classList.add("hidden");
    }
  });
});

//.....................................................Display all products.................................

async function fetchAndDisplayProducts() {
  const url = "https://dummyjson.com/products";
  try {
    const response = await fetch(url);
    const data = await response.json();

    const productsGrid = document.getElementById("products-grid");
    productsGrid.innerHTML = ""; // Clear existing content

    data.products.forEach((product) => {
      const truncatedDescription =
        product.description.length > 30
          ? product.description.substring(0, 70) + "..."
          : product.description;

      const productHTML = document.createElement("div");
      productHTML.className =
        "border border-purple-600 rounded-md shadow-white overflow-hidden";
      productHTML.innerHTML = `
          <div class="p-3">
            <img
              class="w-full h-[250px] object-cover rounded-md"
              src="${product.thumbnail}"
              alt="${product.title}"
            />
            <h1 class="font-sans text-2xl font-bold mt-4 text-purple-500">
              ${product.title}
            </h1>
            <p class="mt-3 text-white font-sans">
              ${truncatedDescription}
            </p>
            <div class="mt-4 font-sans flex justify-between items-center">
              <p class="text-lg font-semibold">$${product.price}</p>
              <button
                class="font-bold bg-purple-700 hover:bg-purple-900 active:bg-violet-700 focus:outline-none focus:ring focus:ring-violet-300 text-white rounded-md px-4 py-2"
                onclick="addToCart(${product.id}, '${product.title}', ${product.price}, '${product.thumbnail}', '${product.description}')"
                >
                Add to Cart
              </button>

            </div>
          </div>
        `;
      productsGrid.appendChild(productHTML);
    });
  } catch (error) {
    console.error("Failed to fetch products:", error);
  }
}

document.addEventListener("DOMContentLoaded", fetchAndDisplayProducts);

//.............................................................Cart list....................................

// Define the cart object globally
let cart = {};

// Attach functions to the window object to ensure global scope accessibility
window.addToCart = function (
  productId,
  productName,
  productPrice,
  thumbnail,
  description
) {
  if (cart[productId]) {
    cart[productId].quantity += 1;
  } else {
    cart[productId] = {
      name: productName,
      price: productPrice,
      thumbnail: thumbnail, // Store thumbnail
      description: description, // Store description
      quantity: 1,
    };
  }
  updateCartUI();
};

window.removeFromCart = function (productId) {
  if (cart[productId] && cart[productId].quantity > 1) {
    cart[productId].quantity -= 1;
  } else {
    delete cart[productId];
  }
  updateCartUI();
};

window.clearCart = function () {
  cart = {};
  updateCartUI();
};

function updateCartUI() {
  const cartItemsContainer = document.getElementById("cart-items");
  cartItemsContainer.innerHTML = ""; // Clear the container first

  let total = 0;
  let totalItems = 0;

  Object.keys(cart).forEach((id) => {
    const item = cart[id];
    total += item.price * item.quantity;
    totalItems += item.quantity;
    const truncatedDescription =
      item.description.length > 70
        ? item.description.substring(0, 70) + "..."
        : item.description;
    const itemHTML = `
<div class="bg-slate-300 order-1 p-2 mb-4 rounded shadow-2xl">
  <div class="flex justify-between items-center">
      <img
          class="w-[100px] h-[100px] object-cover"
          src="${item.thumbnail}"
          alt="${item.name}"
      />
      <div class="flex-1 ml-4">
          <h1 class="text-xl font-semibold text-purple-900">
              ${item.name} - $${item.price.toFixed(2)}
          </h1>
          <p class="mt-1 font-sans text-black">
              ${truncatedDescription}
          </p>
          <div class="flex justify-between items-center mt-2">
              <div class="flex gap-[30px]">
                  <h1 class="text-black font-semibold">Quantity:</h1>
                  <div class="flex items-center justify-center pr-6">
                      <button
                          onclick="window.removeFromCart(${id})"
                          class="bg-gray-400/50 text-black font-bold px-4 text-xl rounded-lg hover:bg-gray-400 focus:outline-none"
                      >
                          -
                      </button>
                      <h1 class="mx-4 text-black text-xl">${item.quantity}</h1>
                      <button
                          onclick="window.addToCart(${id}, '${item.name}', ${
      item.price
    }, '${item.thumbnail}', '${item.description}')"
                          class="bg-gray-400/50 text-black font-bold px-4 text-xl rounded-lg hover:bg-gray-400 focus:outline-none flex items-center justify-center"
                      >
                          +
                      </button>
                  </div>
              </div>
              <p class="text-lg text-black pr-4 font-semibold">
                  $${(item.price * item.quantity).toFixed(2)}
              </p>
          </div>
      </div>
  </div>
</div>
`;
    cartItemsContainer.innerHTML += itemHTML;
  });

  // Update total price and item count display
  document.querySelector(".summary-items-count").textContent = `${totalItems}`;
  document.querySelector(
    ".summary-total-price"
  ).textContent = `$${total.toFixed(2)}`;
}

document.addEventListener("DOMContentLoaded", function () {
  const cartContainer = document.getElementById("shopping-cart");
  const backToShopButton = document.querySelector(".back-to-shop"); // Ensure this button is not dynamically added

  // Using event delegation to handle cart icon clicks
  document.body.addEventListener("click", function (event) {
    // Check if the clicked element or its parent has the 'cart-icon' class
    if (event.target.closest(".cart-icon")) {
      cartContainer.classList.toggle("visible");
    }

    // Close the cart when the "Back to Shop" button is clicked
    if (event.target === backToShopButton) {
      cartContainer.classList.remove("visible");
    }
  });
});
