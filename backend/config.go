package config

import (
	"io/ioutil"

	"gopkg.in/yaml.v2"
)

type Config struct {
	DEX struct {
		URLs   []string `yaml:"urls"`
		Tokens []string `yaml:"tokens"`
	} `yaml:"dex"`
	Risk struct {
		MaxExposure int `yaml:"max_exposure"`
	} `yaml:"risk"`
}

func LoadConfig(path string) (*Config, error) {
	var cfg Config
	data, err := ioutil.ReadFile(path)
	if err != nil {
		return nil, err
	}
	err = yaml.Unmarshal(data, &cfg)
	if err != nil {
		return nil, err
	}
	return &cfg, nil
}
