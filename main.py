import logging
import argparse

LOG_FORMAT = "%(asctime)s %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

action_choices = ["action1", "action2"]


def main() -> None:

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--action", choices=action_choices, required=False, default="action1"
    )
    parser.add_argument("--param1", type=str, default="xpto")

    args = parser.parse_args()

    logging.info(args)


if __name__ == "__main__":
    main()
