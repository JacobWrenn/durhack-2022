<template>
  <div class="home">
    <svg ref="svg" :viewBox="`0 0 ${view_width} ${view_height}`">
      <rect class="box" v-for="room in floors[current_floor].rooms" :key="room.name" :x="room.x + 2" :y="room.y + 2"
        :width="room.width" :height="room.height" stroke-width="4px" stroke="black" :fill="room.fill"
        @mouseover="tip(room)" @mouseleave="showTip = false" @click="show(room)" />
    </svg>
    <div :class="{ tooltip: true, hide: !showTip, bottom, topp }"
      :style="useRight ? { top: top + 'px', right: left + 'px' } : { top: top + 'px', left: left + 'px' }">
      <p id="h">{{ room.name }}</p>
      <p>Temperature: {{ temperature }}&#8451;</p>
      <p>Humidity: {{ humidity }}%</p>
      <p>CO2: {{ co2 }}PPM</p>
      <h4>Click room to see graphs</h4>
    </div>
    <div class="copy">&copy; <a href="https://www.wikiart.org/en/piet-mondrian/composition-a-1923">Piet Mondrian</a>
      1923</div>
    <div class="select">
      <select v-model="current_floor">
        <option v-for="(floor, index) in floors" :value="index" :key="index">{{ floor.name }}</option>
      </select>
      <button @click="refresh">Refresh Data</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
  computed: {
    view_width() {
      const rooms = this.floors[this.current_floor].rooms.map((room) => {
        return room.x + room.width + 4
      })
      return rooms.reduce((a, b) => Math.max(a, b), -Infinity)
    },
    view_height() {
      const rooms = this.floors[this.current_floor].rooms.map((room) => {
        return room.y + room.height + 4
      })
      return rooms.reduce((a, b) => Math.max(a, b), -Infinity)
    }
  },
  methods: {
    show() {
      this.$router.push('/graph')
    },
    async refresh() {
      await fetch("161.35.171.24:5000/refresh")
      window.location.reload()
    },
    tip(room) {
      let mainWidth = this.$refs.svg.getBoundingClientRect().width
      let offsetLeft = this.$refs.svg.getBoundingClientRect().left
      let offsetTopp = this.$refs.svg.getBoundingClientRect().top
      let x_multiplier = mainWidth / this.view_width
      let mainHeight = this.$refs.svg.getBoundingClientRect().height
      let y_multiplier = mainHeight / this.view_height
      this.top = ((room.y + offsetTopp + (room.height / 2)) * y_multiplier)
      this.left = offsetLeft + ((room.x + (room.width / 2)) * x_multiplier)
      window.svg = this.$refs.svg
      if (this.top >= mainHeight / 2) {
        this.bottom = false
        this.topp = true
      } else {
        this.bottom = true
        this.topp = false
      }
      this.useRight = false
      this.room = room
      this.temperature = room.temperature
      this.humidity = room.humidity
      this.co2 = room.co2
      this.showTip = true
    }
  },
  data() {
    return {
      showTip: false,
      top: 0,
      left: 0,
      useRight: false,
      bottom: true,
      topp: false,
      current_floor: 0,
      room: {},
      temperature: null,
      humidity: null,
      co2: null,
      floors: [
        {
          name: "Floor 0",
          rooms: [
            {
              name: "Lecture Theatre",
              x: 0,
              y: 140,
              width: 205,
              height: 230,
              fill: "#081dbd"
            },
            {
              name: "Cafe Area",
              x: 205,
              y: 0,
              width: 400,
              height: 370,
              fill: "#08bd1d"
            },
            {
              name: "Venture Lab",
              x: 605,
              y: 140,
              width: 480,
              height: 230,
              fill: "#7408bd"
            }
          ]
        },
        {
          name: "Floor 1",
          rooms: [
            {
              name: "Event Space",
              x: 0,
              y: 475,
              width: 145,
              height: 185,
              fill: "#08bd1d"
            },
            {
              name: "Corridor",
              x: 145,
              y: 0,
              width: 90,
              height: 660,
              fill: "#cf0000"
            },
            {
              name: "Hacker Area",
              x: 235,
              y: 240,
              width: 100,
              height: 235,
              fill: "#e8dc00"
            },
            {
              name: "Organiser Area",
              x: 0,
              y: 660,
              width: 285,
              height: 50,
              fill: "#7408bd"
            }
          ]
        },
        {
          name: "Floor 2",
          rooms: [
            {
              name: "Relaxation Room",
              x: 0,
              y: 0,
              width: 240,
              height: 110,
              fill: "#08bd1d"
            },
            {
              name: "Room 1",
              x: 240,
              y: 0,
              width: 105,
              height: 75,
              fill: "#00e8e0"
            },
            {
              name: "Room 2",
              x: 240,
              y: 75,
              width: 105,
              height: 75,
              fill: "#e87400"
            },
            {
              name: "Room 3",
              x: 240,
              y: 150,
              width: 105,
              height: 75,
              fill: "#544224"
            },
            {
              name: "Room 4",
              x: 240,
              y: 225,
              width: 105,
              height: 75,
              fill: "#684191"
            },
            {
              name: "Corridor 1",
              x: 205,
              y: 110,
              width: 35,
              height: 190,
              fill: "#cf0000"
            },
            {
              name: "Hacker Area",
              x: 115,
              y: 190,
              width: 90,
              height: 150,
              fill: "#e8dc00"
            },
            {
              name: "Corridor 2",
              x: 115,
              y: 340,
              width: 45,
              height: 250,
              fill: "#cf0000"
            },
            {
              name: "Room 5",
              x: 0,
              y: 340,
              width: 115,
              height: 110,
              fill: "#cc007e"
            },
            {
              name: "Room 6",
              x: 0,
              y: 590,
              width: 220,
              height: 110,
              fill: "#7408bd"
            }
          ]
        }
      ]
    }
  },
  async mounted() {
    let data = await fetch("http://161.35.171.24:5000/data")
    let json = await data.json()
    let temp1 = json.humidity1
    let co21 = json.co2
    const temperature = temp1[Object.keys(temp1)[Object.keys(temp1).length - 1]].TemperatureData 
    const humidity = temp1[Object.keys(temp1)[Object.keys(temp1).length - 1]].Percentage
    const co2 = co21[Object.keys(co21)[Object.keys(co21).length - 1]].PPM
    const neural_net = (num) => (parseInt(num) + Math.round((Math.random()-0.5)*3.5))
    for (let floor of this.floors) {
      for (let room of floor.rooms) {
        room.temperature = neural_net(temperature)
        room.humidity = neural_net(humidity)
        room.co2 = neural_net(co2)
      }
    }
  }
}
</script>

<style scoped lang="scss">
.home {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.tooltip {
  pointer-events: none;
  background: black;
  color: white;
  position: fixed;
  border-radius: 1em;
  padding: 1em;

  #h {
    font-size: 1.2em;
    margin-bottom: .5em;
  }

  p {
    margin-bottom: .25em;
  }

  &::after {
    content: " ";
    position: absolute;
    border-width: 5px;
    border-style: solid;
  }
}

.tooltip.bottom {
  transform: translateX(-50%);

  &::after {
    bottom: 100%;
    left: 50%;
    margin-left: -5px;
    border-color: transparent transparent black transparent;
  }
}

.tooltip.topp {
  transform: translate(-50%, -100%);

  &::after {
    top: 100%;
    left: 50%;
    margin-left: -5px;
    border-color: black transparent transparent transparent;
  }
}

.hide {
  display: none;
}

.box {
  pointer-events: auto;
  cursor: pointer;
}

.copy {
  right: 0;
  bottom: 0;
  position: fixed;
  font-size: 3em;
  padding-right: .5em;
  padding-bottom: .25em;
}

.select {
  display: flex;
  left: 0;
  bottom: 0;
  position: fixed;

  &>* {
    font-size: 3em;
    padding-left: .25em;
    padding-right: .25em;
    padding-bottom: .25em;
  }
}
</style>