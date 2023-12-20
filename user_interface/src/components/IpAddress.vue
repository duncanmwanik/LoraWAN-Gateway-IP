<script setup>
import { ref } from "vue";
import mqtt from "mqtt";

const connected = ref("Not connected to broker.");
const ip = ref("000.000.000.000");

const getIp = () => {
  const client = mqtt.connect("ws://broker.emqx.io:8083/mqtt", {
    log: console.log.bind(console),
    keepalive: 30,
  });

  client.on("connect", () => {
    alert("Connected to MQTT broker.");
    connected.value = "Connected to broker.";

    client.on("message", (topic, message) => {
      ip.value = message.toString();
    });

    client.on("close", () => {
      connected.value = "Not connected to broker.";
    });
  });

  client.subscribe("gateway/id/ip", (err) => {
    if (!err) {
      alert("Subscribed to MQTT topic.");
      connected.value = "Subscribed to MQTT topic.";
    } else {
      alert("Couldn't subscribe to MQTT topic.");
    }
  });
};

//
//
//
</script>

<template>
  <div class="item">
    <div class="details">
      <h3 class="ip-value">{{ ip }}</h3>
      <p>
        Status:

        {{ connected }}
      </p>

      <button class="ip-button" @click="getIp">Get IP</button>

      <slot></slot>
    </div>
  </div>
</template>

<style scoped>
.item {
  margin-top: 2rem;
  display: flex;
  position: relative;
}

.details {
  flex: 1;
  margin-left: 1rem;
}

.ip-value {
  padding: 10px 15px;
  border-radius: 15px;
  border: 1.99px solid hsla(160, 50%, 37%, 1);
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 10px;
}

.ip-button {
  background-color: hsla(160, 100%, 37%, 1);
  color: #fff;
  font-family: Trebuchet MS;
  font-size: 18px;
  font-weight: 800;
  font-style: normal;
  text-decoration: none;
  padding: 10px 60px;
  border: 0px solid #000;
  border-radius: 10px;
  display: inline-block;
  margin-top: 20px;
}

.ip-button:hover {
  background-color: hsla(150, 100%, 37%, 1);
}
.ip-button:active {
  transform: scale(0.95);
}

.close-button {
  background-color: hsla(160, 100%, 37%, 1);
  color: #fff;
  font-family: Trebuchet MS;
  font-size: 18px;
  font-weight: 800;
  font-style: normal;
  text-decoration: none;
  padding: 10px 60px;
  border: 0px solid #000;
  border-radius: 10px;
  display: inline-block;
  margin-top: 20px;
}

i {
  display: flex;
  place-items: center;
  place-content: center;
  width: 32px;
  height: 32px;

  color: var(--color-text);
}

h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: 0xffffff;
}

@media (min-width: 1024px) {
  .item {
    margin-top: 0;
    padding: 0.4rem 0 1rem calc(var(--section-gap) / 2);
  }

  i {
    top: calc(50% - 25px);
    left: -26px;
    position: absolute;
    border: 1px solid var(--color-border);
    background: var(--color-background);
    border-radius: 8px;
    width: 50px;
    height: 50px;
  }

  .item:before {
    content: " ";
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    bottom: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:after {
    content: " ";
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    top: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .item:first-of-type:before {
    display: none;
  }

  .item:last-of-type:after {
    display: none;
  }
}
</style>
