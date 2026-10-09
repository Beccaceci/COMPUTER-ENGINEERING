#!/bin/bash
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INFRA_DIR="$DIR/environment"
COMPOSE_FILE="$INFRA_DIR/docker-compose.yml"

case "$1" in
  start)
    echo "[+] Starting LABINF multi-node environment (Alice, Bob, Chuck)..."
    docker compose -f "$COMPOSE_FILE" up -d
    echo ""
    echo "[+] Environment is active!"
    echo "    - Alice (Server):   10.0.2.10"
    echo "    - Bob   (Client):   10.0.2.20"
    echo "    - Chuck (Attacker): 10.0.2.30"
    echo ""
    echo "Quick terminal access:"
    echo "    ./labinf.sh chuck   -> Kali shell for Chuck"
    echo "    ./labinf.sh bob     -> Kali shell for Bob"
    echo "    ./labinf.sh alice   -> Shell for Alice"
    ;;
  stop)
    echo "[+] Stopping LABINF environment..."
    docker compose -f "$COMPOSE_FILE" down
    echo "[+] Stopped."
    ;;
  restart)
    echo "[+] Restarting LABINF environment..."
    docker compose -f "$COMPOSE_FILE" restart
    ;;
  status)
    docker compose -f "$COMPOSE_FILE" ps
    ;;
  chuck)
    docker exec -it labinf_chuck bash
    ;;
  bob)
    docker exec -it labinf_bob bash
    ;;
  alice)
    docker exec -it labinf_alice bash
    ;;
  read_email)
    docker exec -it labinf_alice cat /var/mail/alice
    ;;
  *)
    echo "LABINF Environment Manager (Politecnico di Torino)"
    echo "Usage: ./labinf.sh {start|stop|restart|status|chuck|bob|alice|read_email}"
    exit 1
    ;;
esac
