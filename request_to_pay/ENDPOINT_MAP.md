# Endpoint Map

This is the description of all API endpoints for the back-end.

## API Docs at `/docs`

## Admin Panel at `/admin`

## RTPBackend at `/api`

### Items at `/items`
 - `/new`
 - `/<int:id>`

### Orders at `/orders`
 - `/new`
 - `/<int:id>`

### Invoices at `/invoices`
 - `/new`
 - `/<int:id>`
 
 - `?status=<string:s>` - UNAVAILABLE

## UserAPI at `/userapi`

### UserProfiles at `/users`
 - `/<int:id>`
 
 - `/<int:id>/notify=<string:s>` - UNAVAILABLE
