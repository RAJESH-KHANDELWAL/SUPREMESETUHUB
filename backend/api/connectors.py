def register_openai_image_adapter() -> None:
    """
    Register the OpenAI Image adapter.

    Provider credentials are validated only when
    the connector is actually executed.
    """

    def generate_image(**payload):
        connector = OpenAIImageConnector()

        return connector.generate(
            **payload
        )

    connector_manager.register_adapter(
        ConnectorAdapter(
            name="openai_image",
            handler=generate_image,
        )
    )


register_openai_image_adapter()
