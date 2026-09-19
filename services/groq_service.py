"""Optional AI-generated weather guidance using Groq."""


class GroqService:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_advice(self, weather):
        if not self.api_key:
            return self._fallback_advice(weather)

        try:
            from groq import Groq

            prompt = (
                "Give one concise, practical weather tip (max 25 words) for: "
                f"{weather['city']}, {weather['temperature']}°C, "
                f"{weather['description']}, humidity {weather['humidity']}%."
            )
            response = Groq(api_key=self.api_key).chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=60,
            )
            return response.choices[0].message.content.strip()
        except Exception:
            return self._fallback_advice(weather)

    @staticmethod
    def _fallback_advice(weather):
        if "rain" in weather["description"].lower():
            return "Take an umbrella and allow extra time for travel."
        if weather["temperature"] >= 30:
            return "Stay hydrated and limit prolonged time in direct sun."
        if weather["temperature"] <= 10:
            return "Wear warm layers before heading outside."
        return "Comfortable conditions—dress in light layers for the day."
