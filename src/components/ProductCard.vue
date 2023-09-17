<template>
<div class="container">
    <div class="card mb-3 h-100" style="width:14rem">
        <img class="card-img-top object-fit-cover" :src=data.image alt="apples" height="200">
        <div class="card-body">
            <b>Apples</b>
            <p class="text-muted my-1">Price: ${{ data.price }}</p>
            <p class="card-text">{{ data.description }}</p>
            <div class="inline-flex">
                <div class="row text-center">
                    <div class="col">
                        <button @click.prevent="doDecrement" class="cartbtn cartbtnleft"><b>-</b></button>
                        <input v-model.number="data.quantity" type="text" class=" cartinput text-center">
                        <button @click.prevent="doIncrement" class="cartbtn cartbtnright"><b>+</b></button>
                        <form @submit.prevent="addToCart" class="mt-2">
                            <button class="btn btn-success btn-sm">Add to Cart</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script setup>
import { reactive } from 'vue';

const data = reactive({
    id: 1,
    name: 'Apples',
    price: 1.99,
    description: 'Kashmir Apples',
    // image: 'https://images.squarespace-cdn.com/content/v1/5b5b5824f2e6b10639fdaf09/1651599956690-0CE43F9HKEXIEK89CY0B/1.png',
    image: 'https://picsum.photos/200/300?random=1',
    quantity: 0,
})

const doIncrement = () => {
    if (data.quantity < 0) data.quantity = 0;
    data.quantity++;
}

const doDecrement = () => {
    if (data.quantity < 0) data.quantity = 0;
    if (data.quantity > 0) {
        data.quantity--;
    }
}

</script>

<style scoped>
.cartbtn {
    border: 1px solid #aaa;
    color: #000;
    padding: 0 8px;
    border-radius: 0;
    border-color:#333;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease-in-out;
}

.cartbtnleft {
    background-color: #ff0000;
    border-radius: 12px 0 0 12px;
}

.cartbtnright {
    background-color: #00ff00;
    border-radius: 0 12px 12px 0;
}

.cartinput {
    width: 3em;
    text-align: center;
    border: 1px solid #888;
    margin: 0px;
    padding: 0px;
    border-radius: 0;
    font-size: 1rem;
    font-weight: 600;
    transition: all 0.3s ease-in-out;
}
</style>