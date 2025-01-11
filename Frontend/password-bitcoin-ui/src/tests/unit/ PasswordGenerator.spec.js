import { mount } from "@vue/test-utils";
import PasswordGenerator from "@/components/PasswordGenerator.vue";
import flushPromises from "flush-promises";

describe("PasswordGenerator.vue", () => {
  it("generates password on button click", async () => {
    const wrapper = mount(PasswordGenerator);

    // Trigger the button click
    await wrapper.find("button").trigger("click");

    // Wait for any asynchronous updates
    await flushPromises();

    // Check if the generated password is updated
    expect(wrapper.vm.generatedPassword).toBeTruthy();
    expect(wrapper.find("input").element.value).toBe(
      wrapper.vm.generatedPassword
    );
  });
});
