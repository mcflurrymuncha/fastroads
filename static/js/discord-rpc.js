/**
 * Discord Rich Presence Integration for fastroads
 * Based on main.e7a33c55.chunk.js
 */

const RPC = require('discord-rpc');
const clientId = '1'; // Replace with your Application ID from Discord Dev Portal
const client = new RPC.Client({ transport: 'ipc' });

// Function to pull data from the game objects
const updatePresence = () => {
    // Check if the game objects are available in the window context
    if (!window.game || !window.z) return;

    const game = window.game;
    const car = window.z;
    
    // 1. Determine Status: Driving or Paused
    const status = game.paused ? "Paused" : "Driving";

    // 2. Get Vehicle Details
    // The 'z' object (Car class) contains vehicle metrics
    const carName = car.metrics ? car.metrics.name : "Unknown Vehicle";

    // 3. Calculate Speed (Game uses m/s, convert to km/h or mph)
    const speedKmh = Math.round(car.speed * 3.6);

    // 4. Track Session Time
    // game.startTime is the unix timestamp when the app launched
    const startTime = game.startTime;

    client.setActivity({
        details: `${status}: ${carName}`,
        state: game.paused ? "In Menus" : `fastroads`,
        startTimestamp: startTime,
        largeImageKey: 'game_logo_large', // Must match Discord Dev Portal assets
        largeImageText: `Game ${window.Zi}`, // Zi is the version constant
        smallImageKey: game.paused ? 'icon_pause' : 'icon_drive',
        instance: false,
    });
};

client.on('ready', () => {
    console.log('Discord Rich Presence is active.');
    
    // Update every 15 seconds to respect Discord rate limits
    setInterval(() => {
        updatePresence();
    }, 15000);

    // Immediate update on pause state change using the game's listener system
    window.game.addStateListener((isPaused) => {
        updatePresence();
    });
});

client.login({ clientId }).catch(console.error);
